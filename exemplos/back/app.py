from flask import Flask, jsonify

app = Flask(__name__)


@app.get("/health")
def health():
    return jsonify(status="ok")


@app.get("/predict")
def predict():
    # Placeholder: aqui entraria o modelo de ML carregado.
    return jsonify(resultado=0.87)
