import socket
from flask import Flask, jsonify

app = Flask(__name__)
counter = 0  # in-memory: resets when container restarts (that's fine, and a lesson)

@app.route("/api/count")
def count():
    global counter
    counter += 1
    return jsonify(hostname=socket.gethostname(), count=counter)

@app.route("/health")
def health():
    return jsonify(status="ok")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=False)