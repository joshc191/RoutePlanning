# RoutePlanning
By Chris Cho, Josh Cho, Alhassan Natah

This repository consists of a website where mobile grocery stores or food trucks can plan their route through the city. The project was done as the final project for the course ENGO 551.

<Insert website link>

## Description
The website's main page contains a webmap of Calgary, along with a form.
- Users can input a list of locations (customer addresses) into the form.
- The website will use clustering and shortest path algorithms to find the most efficient route for the truck.

The website also has a RESTful API backend, where users can make GET requests to the website by providing a list of addresses and number of stops. The website will output a list of coordinates for the route stops.

## How to run
1. Install a copy of [Python](https://www.python.org/downloads/) if you haven't already. Version 3.6 or higher is recommended
2. Install [pip](https://pip.pypa.io/en/stable/installing/) if you haven't already.
3. Download/pull repository
4. Run ```pip3 install -r requirements.txt``` to install all necessary Python packages.
5. Set the environment variable ```FLASK_APP``` to be ```application.py```.
    - Windows: ```set FLASK_APP=application.py```
    - Mac/Linux: ```export FLASK_APP=application.py```  
6. Optionally, if debugging, run ```set FLASK_DEBUG=1``` to automatically update the website when changes are made.
7. Run ```flask run``` to start the Flask application.

## Contents
- application.py: main script for Flask application
- functions.py: function definitions for application.py
- requirements.txt: lists packages needed to run application
- static: contains assest for html pages
  - styles
    - styles.css: defines styles in index.html
- templates: contains html templates for flask app
  - index.html: template for website's main page
  - docs.html: template for website's API documentation
- csv files (sample_addresslist.csv, sample_addresslist2.csv, etc): Sample address lists for website

## TO DO
- index.html
  - Add sidebar for directions + route travel time

- Misc
  - Add link to docs.html in navigation bar
  - Add table/widget to allow for address list changes within website
  - Add error handling for incorrect API calls
  - Handle error when first address can't be found

- Current Bugs

## References
- OpenCalgary [Parcel Addresses Dataset](https://data.calgary.ca/Base-Maps/Parcel-Address/9zvu-p8uz)
- OpenCalgary [Business Licenses Dataset](https://dev.socrata.com/foundry/data.calgary.ca/vdjc-pybd)
- Travelling Salesman Problem: [Google OR-Tools](https://developers.google.com/optimization/routing/tsp)
- Mapbox [Directions API](https://docs.mapbox.com/api/navigation/directions/)
