# RoutePlanning
By Chris Cho, Josh Cho, Alhassan Natah

This repository consists of a website where mobile grocery stores or food trucks can plan their route through the city. The project was done as the final project for the course ENGO 551.

<Insert website link>

## Description
The website's main page contains a webmap of Calgary, along with a form.
- Users can input a list of locations (customer addresses) into the form.
- The website will use clustering and shortest path algorithms to find the most efficient route for the truck.

The website also has a RESTful API backend, where users can make GET requests to the website by providing a list of addresses and number of stops. The website will output a list of coordinates for the route stops.

## TO DO

- Design website (CSS)
- Set up flask

- index.html
  - Get Mapbox directions through each stop
  - Add sidebar for directions + route travel time

- API.html
  - Get directions from stops using directions API

- API_docs.html
  - Document API

- Misc
  - Improve csv reader
    - Handle blank lines at end of files
    - Handle invalid addresses
  - Add table/widget to allow for address list changes within website
  - Add labels for address markers
  - Add error handling for incorrect API calls
  - Add error handling when stop numbers exceed address number

- Current Bugs

## References
- Travelling Salesman Problem: [Google OR-Tools](https://developers.google.com/optimization/routing/tsp)
