from flask import Flask
app = Flask(__name__)

@app.route('/cheese')
def hello_cheese():
    return 'Hello, cheese'