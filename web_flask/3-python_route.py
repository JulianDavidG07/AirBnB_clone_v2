#!/usr/bin/python3

"""
Script that starts a Flask web application:

Your web application must be listening on 0.0.0.0, port 5000
Routes:
    /: display “Hello HBNB!”
    /hbnb: display “HBNB”
    /c/<text>: display “C ”, followed by the value of the text variable
    (replace underscore _ symbols with a space )
    /python/(<text>): display “Python ”, followed by the
        value of the text variable
        (replace underscore _ symbols with a space )
        The default value of text is “is cool”
"""


from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def page():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def more(text):
    return 'C ' + text.replace('_', ' ')


@app.route('/python/')
@app.route('/python/<fix>', strict_slashes=False)
def fixed(fix='is_cool'):
    return 'Python ' + fix.replace('_', ' ')


if __name__ == "__main__":
    app.run(host='0.0.0.0')
