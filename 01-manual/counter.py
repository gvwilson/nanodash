"""Counter server."""

from flask import Flask
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

STATE = {
    "value": 0
}

@app.route("/")
def index():
    """Display message"""
    STATE["value"] += 1
    return f"count: {STATE['value']}"
