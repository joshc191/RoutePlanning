# RoutePlanning
By Chris Cho, Josh Cho, Alhassan Natah
This repository consists of a website where mobile grocery stores or food trucks can plan their route through the city. The project was done as the final project for the course ENGO 551.

<Insert website link>

## Description
The website's main page contains a webmap of Calgary, along with a form.
- Users can input a list of locations (lat,lon) into the form.
- The website will use clustering and shortest path algorithms to find the most efficient route for the truck.

The website also has a RESTful API backend, where users can make GET requests to the website by providing a list of coordinates in GeoJSON format. The website will output a list of coordinates for the route in GEOJSON polyline format.
