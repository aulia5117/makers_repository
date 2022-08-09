# Latihan 6

import requests, base64
from flask import Flask, request

app = Flask(__name__)

@app.route("/cat-and-mouse/x/<input_x>")

def catAndMouse(input_x):
    x = int(input_x)
    y = int(request.args.get("y"))
    z = int(request.headers.get('z'))
    
    if abs(z-x) < abs(z-y) :
        message = "Cat A"
    elif abs(z-y) < abs(z-x) :
        message = "Cat B"
    elif abs(z-y) == abs(z-x) :
        message = "Mouse C"
    return {
        "x" : x,
        "y" : y,
        "z" : z,
        "message" : message
        }