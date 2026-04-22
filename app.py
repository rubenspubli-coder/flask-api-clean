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
@app.route("/api/chat", methods=["POST"])
def chat():
    from flask import Response
    import json

    data = request.get_json()
    messages = data.get("messages", [])

    last_user = ""
    if messages:
        last = messages[-1]
        if isinstance(last.get("content"), str):
            last_user = last["content"]

    # lógica de resposta
    if last_user == "start":
        text = "Bem-vindo ao Sports Studio, onde a mágica acontece! Digite a senha de acesso:"
    elif last_user.strip().lower() == "pablo":
        text = "Vamos nessa! Agora descreva o que você deseja criar e use o botão de imagem para anexar a foto do atleta de referência."
    else:
        text = "Senha incorreta."

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
