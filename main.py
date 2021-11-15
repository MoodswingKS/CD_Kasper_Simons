from flask import Flask

main = Flask(__name__)

@main.route("/")
def index():
    return "De laatste opdracht"


@main.route("/kasper")
def cow():
    return "Lekker gewandeld"