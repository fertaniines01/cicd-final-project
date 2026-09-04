"""
Counter Service - application minimale pour le projet CI/CD.
"""
from flask import Flask, jsonify

app = Flask(__name__)

counter = {"count": 0}


@app.route("/health", methods=["GET"])
def health():
    """Vérifie que le service tourne."""
    return jsonify({"status": "SERVICE RUNNING"}), 200


@app.route("/counter", methods=["GET"])
def get_counter():
    """Retourne la valeur actuelle du compteur."""
    return jsonify(counter), 200


@app.route("/counter/increment", methods=["POST"])
def increment_counter():
    """Incrémente le compteur de 1."""
    counter["count"] += 1
    return jsonify(counter), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
