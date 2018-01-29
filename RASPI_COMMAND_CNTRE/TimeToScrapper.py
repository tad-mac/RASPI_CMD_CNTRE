#!/usr/bin/env python

"""
This webscrapper uses the Google Maps API to display the time it would take to
travel to two different locations. This information is then used in the main
program where it is displayed in a QLabel.

"""

import simplejson as json
import requests

# Enter your Google API Key Here
key = "&key= "


def TimeTo(beginning, ending):

    # Grabs the time to travel between the two points

    PointA = beginning.replace(" ", "+")
    PointB = ending.replace(" ", "+")

    api_base = "https://maps.googleapis.com/maps/api/distancematrix/json?"
    units = "units=metric"
    start = "&origins=" + PointA
    end = "&destinations=" + PointB
    tolls = "&avoid=tolls"

    r = requests.get(api_base + units + start + end + tolls + key)

    if r.status_code == 200:
        time = json.loads(r.text)["rows"][0]["elements"][0]["duration"]["text"]
        return time
    else:
        return "Error"
