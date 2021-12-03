from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "De laatste opdracht"


@app.route("/kasper")
def kasper():
    return "Lekker gewandeld pik"

if __name__ == "__main__":
    app.run()