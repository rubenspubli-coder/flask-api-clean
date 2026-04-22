from flask import Flask, request, jsonify, send_file

app = Flask(__name__)

# =========================
# FRONTEND
# =========================
@app.route("/")
def serve_frontend():
    return send_file("frontend/index.html")


# =========================
# API CHAT
# =========================
import os
import requests
from flask import Response
import json

@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.get_json()
    messages = data.get("messages", [])

    api_key = os.getenv("ANTHROPIC_API_KEY")

    last_user = ""
    if messages:
        last = messages[-1]
        if isinstance(last.get("content"), str):
            last_user = last["content"]

    # 🔐 verifica se já autenticou antes
    authenticated = any(
        isinstance(m.get("content"), str) and m["content"].strip().lower() == "pablo"
        for m in messages
    )

    # primeira mensagem
    if last_user == "start":
        text = "Bem-vindo ao Sports Studio, onde a mágica acontece! Digite a senha de acesso:"

    # ainda não autenticado
    elif not authenticated:
        if last_user.strip().lower() == "pablo":
            text = "Vamos nessa! Agora descreva o que você deseja criar e use o botão de imagem para anexar a foto do atleta de referência."
        else:
            text = "Senha incorreta."

    # já autenticado → chama Claude
    else:
        response = requests.post(
            "https://api.anthropic.com/v1/messages",
            headers={
                "x-api-key": api_key,
                "anthropic-version": "2023-06-01",
                "content-type": "application/json"
            },
            json={
                "model": "claude-3-sonnet-20240229",
                "max_tokens": 2000,
                "messages": messages,
                "system": data.get("system", "")
            }
        )

        res_json = response.json()
        text = res_json["content"][0]["text"]

    # streaming response
    def generate():
        chunk = {
            "type": "content_block_delta",
            "delta": {
                "type": "text_delta",
                "text": text
            }
        }
        yield f"data: {json.dumps(chunk)}\n\n"
        yield "data: [DONE]\n\n"

    return Response(generate(), mimetype="text/event-stream")

# =========================
# START
# =========================
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
