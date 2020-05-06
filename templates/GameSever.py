from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


@app.route("/")
def serveCards():
    return "hello"
    
    


