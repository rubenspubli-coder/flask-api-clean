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
    data = request.get_json()
    messages = data.get("messages", [])

    last_user = ""
    if messages:
        last = messages[-1]
        if isinstance(last.get("content"), str):
            last_user = last["content"]

    # PRIMEIRA MENSAGEM (boot)
    if last_user == "start":
        return jsonify({
            "content": [
                {
                    "text": "Bem-vindo ao Sports Studio, onde a mágica acontece! Digite a senha de acesso:"
                }
            ]
        })

    # SENHA CORRETA
    if last_user.strip().lower() == "pablo":
        return jsonify({
            "content": [
                {
                    "text": "Vamos nessa! Agora descreva o que você deseja criar e use o botão de imagem para anexar a foto do atleta de referência."
                }
            ]
        })

    # SENHA ERRADA
    return jsonify({
        "content": [
            {
                "text": "Senha incorreta."
            }
        ]
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
