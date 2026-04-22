import os
from flask import Flask, jsonify

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "fallback-dev-key")


@app.route("/")
def home():
    return jsonify({"message": "Hello, CI/CD!"})


@app.route("/health")
def health():
    return jsonify({"status": "ok"}), 200


@app.route("/version")
def version():
    return (
        jsonify(
            {
                "version": "1.0.0",
                "environment": os.environ.get("FLASK_ENV", "production"),
            }
        ),
        200,
    )


if __name__ == "__main__":
    from dotenv import load_dotenv

    load_dotenv()
    app.run(host="0.0.0.0", port=5000)  # nosec B104
