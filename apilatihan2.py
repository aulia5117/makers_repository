# Latihan 2

from flask import Flask, request

app = Flask(__name__)

@app.route('/hello-json', methods='GET')
def hello():
    a = request.args.get('message')
    return {
        "message" : "Hello " + a
    }

# print(hello())