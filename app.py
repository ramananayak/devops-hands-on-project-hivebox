from flask import Flask
import os

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hellow Dynamic devops roadmap"


def read_version():
    return os.environ["APP_VERSION"]


@app.route("/version")
def print_version():
    return read_version()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
