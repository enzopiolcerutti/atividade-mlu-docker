import os
import joblib
import numpy as np
from flask import Flask, jsonify, request

MODEL_PATH = os.getenv("MODEL_PATH", "/models/model.joblib")

app = Flask(__name__)
artifact = None

def load_model():
    global artifact
    if artifact is None and os.path.exists(MODEL_PATH):
        artifact = joblib.load(MODEL_PATH)
    return artifact


@app.get("/health")
def health():
    return jsonify(status="ok", model_loaded=load_model() is not None)


@app.post("/predict")
def predict():
    art = load_model()
    if art is None:
        return jsonify(error=f"modelo não encontrado em {MODEL_PATH}"), 503

    closes = (request.get_json(silent=True) or {}).get("closes")
    n = art["n_lags"]
    if not isinstance(closes, list) or len(closes) != n:
        return jsonify(error=f"envie 'closes' com {n} valores numericos"), 400
    try:
        x = np.array(closes, dtype=float).reshape(1, -1)
    except (TypeError, ValueError):
        return jsonify(error="valores devem ser numericos"), 400

    pred = float(art["model"].predict(x)[0])
    return jsonify(prediction=pred, model=art["name"], disclaimer="experimental, nao considere como recomendacao")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
