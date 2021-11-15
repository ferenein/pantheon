from flask import Flask
from src import get_sentence

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello</h1>'


@app.route('/madlib')
def madlib():
    return get_sentence()


if __name__ == '__main__':
    from waitress import serve
    serve(app, host="0.0.0.0", port=5000)

    # app.run(debug=True, host='0.0.0.0')

