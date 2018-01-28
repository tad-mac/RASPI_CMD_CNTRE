import simplejson as json
import requests

# Enter your Google API Key Here
key = ""

# First slot for time to destination 1


def Slot1():
    start = "New+York"
    end = "San+Fransico"

    r = requests.get("https://maps.googleapis.com/maps/api/distancematrix/json?units=metric&origins=" +
                     start + "&destinations=" + end + "&avoid=tolls&key=" + key)
    time = json.loads(r.text)["rows"][0]["elements"][0]["duration"]["text"]
    # These Lines are used fro debugging
    # print("Status", r.status_code)
    # print(r.text)
    # print(time)
    return time

# Second slot for time to  destination 2


def Slot2():
    start = "London,England"
    end = "Paris,France"
    r = requests.get("https://maps.googleapis.com/maps/api/distancematrix/json?units=metric&origins=" +
                     start + "&destinations=" + end + "&avoid=tolls&key=" + key)
    time = json.loads(r.text)["rows"][0]["elements"][0]["duration"]["text"]
    # These Lines are used fro debugging
    # print("Status", r.status_code)
    # print(r.text)
    # print(time)
    return time
