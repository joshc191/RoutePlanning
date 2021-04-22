import os
import requests

from flask import Flask, session, render_template, redirect, request, jsonify, url_for
from flask_session import Session

from functions import getRoute, travellingSalesman, coordStringtoDouble, getDirections
import numpy as np

app = Flask(__name__)

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api", methods = ['GET'])
def api():
    addresslist = request.args.get('addresslist')
    stopnum = request.args.get('stopnum')

    route = getRoute(addresslist, stopnum)
    route2, instructions = getDirections(route)
    return jsonify({
        "type": "Feature",
        "properties": {
            "directions": instructions
        },
        "geometry": {
            "coordinates": route2,
            "type": "LineString"
        }
    })

@app.route("/docs")
def docs():
    return render_template("docs.html")

#background process to compute re-order stops (travelling salesman solution)
@app.route('/reorder_stops/<coords>', methods = ['GET'])
def reorder_stops(coords):
    coords_arr = coordStringtoDouble(coords)
    route = travellingSalesman(coords_arr)
    return jsonify({"coordinates": np.array2string(route)})
