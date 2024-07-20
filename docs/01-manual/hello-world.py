"""Basic Flask 'hello, world' server."""

from flask import Flask
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


@app.route("/")
def index():
    """Display message"""
    return "hello, world"
