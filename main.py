#!/bin/env python
from flask import Flask, request
app = Flask(__name__)


trusted_user_agent = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:127.0) Gecko/20100101 Firefox/127.'
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
