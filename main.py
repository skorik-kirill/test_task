from flask import Flask, request
app = Flask(__name__)

@app.route('/hello')
def hello():
  message = 'Hello, Prozzorro!'
  return message


if __name__ == '__main__':
   app.run()
