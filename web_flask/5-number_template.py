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
        /number/<n>: display “n is a number” only if n is an integer
            H1 tag: “Number: n” inside the tag BODY
"""


from flask import Flask
from flask import render_template

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


@app.route('/number/<int:num>', strict_slashes=False)
def integer(num):
    if isinstance(num, int):
        return str(num) + ' is a number'


@app.route('/number_template/<int:n>', strict_slashes=False)
def number(n):
    if isinstance(n, int):
        return render_template('5-number.html', number=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
