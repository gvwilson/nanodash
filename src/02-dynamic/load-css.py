"""CSS server."""

from flask import Flask, jsonify
from flask_cors import CORS
import os


# Appliction factory
def create_app():
    app = Flask(__name__)
    CORS(app)

    @app.route("/")
    def css():
        try:
            filename = os.getenv("CSS", "default.css")
            with open(filename, "r") as reader:
                return reader.read()
        except OSError as exc:
            return f"Unable to read {filename}: {exc}", 500

    return app
