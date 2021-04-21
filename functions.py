import urllib.parse as urlparse
from urllib.parse import parse_qs

from sklearn.cluster import KMeans
from scipy.spatial import distance_matrix
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp
import numpy as np

import requests


def getcoords(address):
    """Get GeoJSON information for a parcel by sending GET request to OpenCalgary Parcel Address Dataset."""
    link = "https://data.calgary.ca/resource/9zvu-p8uz.geojson?$q=" + "\'" + address + "\'";
    res = requests.get(link)
    if res.status_code != 200:
        raise Exception("Error: API request unsuccessful.")
    data = res.json()
    return data


def travellingSalesman(stops):
    """Order stops by solving travelling salesman problem
    (https://developers.google.com/optimization/routing/tsp)"""
    # get distances between all stops
    dist_mat = distance_matrix(stops, stops)

    manager = pywrapcp.RoutingIndexManager(len(stops), 1, 0)    # args: number of stops, number of vehicles, depot num
    routing = pywrapcp.RoutingModel(manager)

    def distance_callback(from_index, to_index):
        """Returns the distance between the two nodes."""
        # Convert from routing variable Index to distance matrix NodeIndex.
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return dist_mat[from_node][to_node]

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()   # Setting first solution heuristic
    search_parameters.first_solution_strategy = routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC

    solution = routing.SolveWithParameters(search_parameters)   # Solve the TS problem
    route_order = getRouteOrder(solution, routing, manager)[0]

    # Get re-ordered list of stops
    stops_ordered = stops[route_order]
    stops_ordered = np.delete(stops_ordered, -1, 0)  # Remove last stop (the starting point)
    return stops_ordered


def getRouteOrder(solution, routing, manager):
    """Get vehicle routes from a solution and store them in an array."""
    # Get vehicle routes and store them in a two dimensional array whose
    # i,j entry is the jth location visited by vehicle i along its route.
    routes = []
    for route_nbr in range(routing.vehicles()):
        index = routing.Start(route_nbr)
        route = [manager.IndexToNode(index)]
        while not routing.IsEnd(index):
            index = solution.Value(routing.NextVar(index))
            route.append(manager.IndexToNode(index))
        routes.append(route)
    return routes


def getRoute(query):
    """Get truck route from the user's query."""
    # get parameters from query
    parsed = urlparse.urlparse(query)
    parsed_q = parse_qs(parsed.query)
    addresslist = parsed_q['addresslist'][0]
    stopnum = int(parsed_q['stopnum'][0])

    # separate addresses in addresslist
    addresslist = addresslist.replace('\'', '')  # Remove apostrophes
    addresslist = addresslist.replace('\"', '')  # Remove quotes
    addresslist_spl = addresslist.split(", ")
    if len(addresslist_spl) < 2:
        addresslist_spl = addresslist.split(",")
    addresslist = addresslist_spl

    # get coordinates of addresses in addresslist
    coordslist = []
    for address in addresslist:
        parceldata = getcoords(address)
        coordslist.append(parceldata['features'][0]['geometry']['coordinates'])

    # do kmeans clustering to get stops from addresslist
    kmeans = KMeans(n_clusters=stopnum, random_state=0).fit(np.array(coordslist))
    stops = kmeans.cluster_centers_

    # add first address in address list (ie where the truck starts the day)
    stops2 = np.insert(stops, 0, coordslist[0], axis=0)
    print(stops2)

    # Solve travelling salesman problem to re-order stops into optimal order
    stops_ordered = travellingSalesman(stops2)
    return stops_ordered


def coordStringtoDouble(string):
    """Convert coordinates in string format to double"""
    string = string.replace('\'', '')  # Remove apostrophes
    string = string.replace('\"', '')  # Remove quotes
    string_sp = string.split(',')
    stopnum = int(len(string_sp) / 2)
    coords = np.empty([stopnum, 2])
    for i in range(0, stopnum, 1):
        coords[i, :] = np.array([string_sp[2*i], string_sp[2*i+1]])
    return coords


def main():
    """Test function defined above"""
    # query = '?addresslist=\'11650 18 ST NE, 390 SADDLECREST CI NE, 165 SADDLEHORN CR NE, 1228 CORNERSTONE WY NE, 61 CORNER MEADOWS GD NE, 161 SADDLELAKE TC NE, 23 HARVEST ROSE CI NE, 355 CORNER MEADOWS AV NE, 54 SAVANNA DR NE, 2312 MILLWARD RD NE, 2720 CENTRE ST NE, 42 TEMPLE PL NE, 75 CITYSCAPE GV NE, 119 TEMPLEVALE PL NE\'&stopnum=5'
    # route = getRoute(query)

    coords = coordStringtoDouble('-114.04556762766781,51.1256171832884,-113.93705706740492,51.13238575074399,-113.96809112063988,51.07894723738647,-113.92696893267832,51.14948303565794,-113.96568985100154,51.1444119580011')
    route = travellingSalesman(coords)
    print(route)

if __name__ == "__main__":
    main()
