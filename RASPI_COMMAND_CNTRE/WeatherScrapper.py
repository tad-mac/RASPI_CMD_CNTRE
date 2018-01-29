#!/usr/bin/env python

"""

"""

import requests
import simplejson as json

# Enter your Wunderground API key here
api_key = "api/"
api_base = "http://api.wunderground.com/"
location = "q/pws:KNYBROOK40.json"

r = requests.get(api_base + api_key + "/conditions/" + location)

data = json.loads(r.text)
# print(data)


def temperature():

    temp = json.loads(r.text)["current_observation"]["temp_c"]
    print(temp, "C")
    output = str(temp)
    output = output + " C"
    return output


def conditions():

    statement = json.loads(r.text)["current_observation"]["weather"]
    print("Today it is", statement.lower())
    output = statement.lower()
    output = "Today it is " + output
    return output
