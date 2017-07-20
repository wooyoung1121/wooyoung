from flask import Flask
app = Flask(__name__)

@app.route('/<name>/<lastname>')
def hello(name,lastname):
    return 'hello %s %s' % (name, lastname)

if __name__ == '__main__':
      app.run(host='0.0.0.0', port=8080)