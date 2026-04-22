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
from flask import Flask, request, jsonify, send_file

app = Flask(__name__)

ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")

# =========================
# FRONTEND
# =========================
@app.route("/")
def serve_frontend():
    return send_file("frontend/index.html")


# =========================
# API CHAT
# =========================
@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.get_json()
    messages = data.get("messages", [])

    last_user = ""
    if messages:
        last = messages[-1]
        if isinstance(last.get("content"), str):
            last_user = last["content"]

    # BOOT
    if last_user == "start":
        return jsonify({
            "content": [{"text": "Bem-vindo ao Sports Studio, onde a mágica acontece! Digite a senha de acesso:"}]
        })

    # SENHA
    if last_user.strip().lower() == "pablo":
        return jsonify({
            "content": [{"text": "Vamos nessa! Agora descreva o que você deseja criar e use o botão de imagem para anexar a foto do atleta de referência."}]
        })

    # =========================
    # CHAMADA REAL DO CLAUDE
    # =========================
    try:
        response = requests.post(
            "https://api.anthropic.com/v1/messages",
            headers={
                "x-api-key": ANTHROPIC_API_KEY,
                "anthropic-version": "2023-06-01",
                "content-type": "application/json"
            },
            json={
                "model": "claude-3-haiku-20240307",
                "max_tokens": 1000,
                "messages": [
                    {
                        "role": "user",
                        "content": last_user
                    }
                ]
            }
        )

        result = response.json()

        text = result.get("content", [{}])[0].get("text", "Erro ao gerar resposta.")

        return jsonify({
            "content": [{"text": text}]
        })

    except Exception as e:
        return jsonify({
            "content": [{"text": f"Erro Claude: {str(e)}"}]
        })


# =========================
# DEBUG
# =========================
@app.route("/debug")
def debug():
    return {"status": "ok"}


# =========================
# START
# =========================
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)

# =========================
# START
# =========================
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
