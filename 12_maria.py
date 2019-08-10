import requests
import json
import time
from math import radians, cos, sin, asin, sqrt, atan2, degrees


def get_position():
    url = 'http://api.open-notify.org/iss-now.json'
    response = requests.get(url)
    response.raise_for_status()
    response_content = json.loads(response.text)
    timestamp = response_content['timestamp']
    position = response_content['iss_position']
    latitude = position['latitude']  # add unpacking
    longitude = position['longitude']

    return float(latitude), float(longitude), timestamp


def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a))
    r = 6371  # Radius of earth in kilometers. Use 3956 for miles
    return c * r


# LICENSE: public domain

def calculate_initial_compass_bearing(pointA, pointB):
    """
    Calculates the bearing between two points.
    The formulae used is the following:
        θ = atan2(sin(Δlong).cos(lat2),
                  cos(lat1).sin(lat2) − sin(lat1).cos(lat2).cos(Δlong))
    :Parameters:
      - `pointA: The tuple representing the latitude/longitude for the
        first point. Latitude and longitude must be in decimal degrees
      - `pointB: The tuple representing the latitude/longitude for the
        second point. Latitude and longitude must be in decimal degrees
    :Returns:
      The bearing in degrees
    :Returns Type:
      float
    """
    if (type(pointA) != tuple) or (type(pointB) != tuple):
        raise TypeError("Only tuples are supported as arguments")

    lat1 = radians(pointA[0])
    lat2 = radians(pointB[0])

    diffLong = radians(pointB[1] - pointA[1])

    x = sin(diffLong) * cos(lat2)
    y = cos(lat1) * sin(lat2) - (sin(lat1)
                                 * cos(lat2) * cos(diffLong))

    initial_bearing = atan2(x, y)

    # Now we have the initial bearing but atan2 return values
    # from -180° to + 180° which is not what we want for a compass bearing
    # The solution is to normalize the initial bearing as shown below
    initial_bearing = degrees(initial_bearing)
    compass_bearing = (initial_bearing + 360) % 360

    return compass_bearing


latitude, longitude, time1 = get_position()
time.sleep(1)
latitude1, longitude1, time2 = get_position()

distance = haversine(longitude, latitude, longitude1, latitude1)
direction = calculate_initial_compass_bearing((latitude, longitude), (latitude1, longitude1))

time_delta = time2 - time1
speed = distance * time_delta

print('distance: ' + str(distance) + ' km', 'speed: ' + str(speed) + ' km/s', 'time delta: ' + str(time_delta))
