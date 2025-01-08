from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, world!</p>"

