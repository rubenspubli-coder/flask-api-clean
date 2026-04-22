from flask import Flask, request, jsonify, send_file

app = Flask(__name__)

# FRONTEND
@app.route("/")
def serve_frontend():
    return send_file("frontend/index.html")


# API CHAT (ESSA QUE FALTAVA)
@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.get_json()
    messages = data.get("messages", [])

    last_user = ""
    if messages:
        last = messages[-1]
        if isinstance(last.get("content"), str):
            last_user = last["content"]

    # lógica da senha
    if "Pablo" in last_user:
        return jsonify({
            "content": [
                {"text": "Vamos nessa! Agora descreva o que você deseja criar e use o botão de imagem para anexar a foto do atleta de referência."}
            ]
        })

    return jsonify({
        "content": [
            {"text": "Senha incorreta."}
        ]
    })


# DEBUG
@app.route("/debug")
def debug():
    return {"status": "ok"}
