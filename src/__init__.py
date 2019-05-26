from flask import Flask, render_template, session

from src import config


def create_app():

    app = Flask(__name__)
    app.config.from_object(config)
    app.secret_key = "sdshfh923eew8/*+-1#$%^^!*"

    return app
