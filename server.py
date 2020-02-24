from flask import Flask
app = Flask(__name__)


@app.route("/")
def index():
    return '<h1>Why liddat?</h1>'


@app.route("/another")
def show():
    return '<h1> Yo this is your another page</h1>'


if __name__ == '__main__':
    app.run()
