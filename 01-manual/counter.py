"""Counter server."""

from flask import Flask
from flask_cors import CORS


def create_app():
    """Application factory (called by Flask automatically)."""
    app = Flask(__name__)
    CORS(app)

    state = {
        "value": 0
    }

    @app.route("/")
    def index():
        """Display message"""
        state["value"] += 1
        return f"count: {state['value']}"

    return app
