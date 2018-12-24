from flask import Flask

app = Flask("wtf")

@app.route("/<name>")
def index(name):
    if name.lower() == "bruno":
        return "Olá {}".format(name)
    else:
        return "Not Found"

