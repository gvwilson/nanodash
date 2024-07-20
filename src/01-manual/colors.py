"""Color server."""

from flask import Flask, jsonify
from flask_cors import CORS
import random
import os


# Seed random number generation using environment variable
seed = os.getenv('SEED')
random.seed(None if seed is None else int(seed))


# Appliction factory
def create_app():
    app = Flask(__name__)
    CORS(app)

    @app.route("/")
    def index():
        """Create random hex color."""
        return jsonify(
            red=random.randint(0, 255),
            green=random.randint(0, 255),
            blue=random.randint(0, 255),
        )

    return app
