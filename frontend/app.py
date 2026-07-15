import os
import requests
from flask import Flask, render_template

app = Flask(__name__)
BACKEND_URL = os.environ.get("BACKEND_URL", "http://localhost:5001")

@app.route("/")
def index():
    try:
        data = requests.get(f"{BACKEND_URL}/api/count", timeout=2).json()
        return render_template("index.html", hostname=data["hostname"],
                               count=data["count"], error=None)
    except requests.exceptions.RequestException as e:
        return render_template("index.html", hostname=None, count=None, error=str(e))

@app.route("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=False)