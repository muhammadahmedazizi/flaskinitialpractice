from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello_world():
    return "Hello, Ahmed Bhai Jan"

@app.route('/about')
def about():
    return "We are a multinational company"