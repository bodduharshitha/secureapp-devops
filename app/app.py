from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify(
        application="SecureApp",
        message="DevOps platform is running"
    )


@app.route("/health")
def health():
    return jsonify(
        status="healthy"
    )


@app.route("/info")
def info():
    return jsonify(
        application="secureapp",
        version="1.0.0",
        environment="development"
    )

@app.route("/harshu")
def harshu():
    return jsonify(
        message="Hello, Harshu!"
    )


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )