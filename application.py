import os
import requests

from flask import Flask, session, render_template, redirect, request, jsonify
from flask_session import Session

from functions import getRoute

app = Flask(__name__)

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/")
def index():
    # stuff
    return render_template("index.html")

@app.route("/api/<query>")
def api(query):
    route = getRoute(query)
    return route

@app.route("/docs")
def docs():
    # stuff
    return render_template("docs.html")
