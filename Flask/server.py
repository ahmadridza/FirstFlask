from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def index():
    signed_in = False
    return render_template('index.html', signed_in=signed_in)


@app.route("/another")
def show1():
    return '<h1> Yo this is your another page</h1>'


@app.route('/user/<username>')
def show(username):
    return f"Hi {username[5]}"


if __name__ == '__main__':
    app.run(debug=True)
