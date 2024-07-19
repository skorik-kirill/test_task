#!/usr/bin/python3
from flask import Flask, request
app = Flask(__name__)


trusted_user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
bad_guy = 'fishing site'

@app.route('/hello')
def hello():
  response = request.headers.get('User-Agent')
  print(response)
  if response != trusted_user_agent or response == bad_guy:
     message = '403'
  else:
     message = 'Hello, Prozzorro!'
  return message, response
   

if __name__ == '__main__':
   app.run()
