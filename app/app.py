from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)


@app.route("/health")
def health():

    return jsonify({
        "status": "running",
        "service": "automation-api",
        "timestamp": datetime.now().isoformat()
    })


@app.route("/")
def home():

    return "Cyber Resilience Platform API"


if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000
    )