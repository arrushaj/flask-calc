from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.get('/add')
def addition():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))

    return f"<html><body><h1>{add(a,b)}</h1></body></html>"

@app.get('/sub')
def subtraction():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))

    return f"<html><body><h1>{sub(a,b)}</h1></body></html>"

@app.get('/mult')
def multiply():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))

    return f"<html><body><h1>{mult(a,b)}</h1></body></html>"

@app.get('/div')
def divide():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))

    return f"<html><body><h1>{div(a,b)}</h1></body></html>"

