
import requests
import json

BASE_URL = "http://127.0.0.1:5000/api"


def get_routes():
    response = requests.get(BASE_URL + "/routes")
    return response.content

def update_routes():

    new_route = {
        "trade_name": "Золото партии",
        "city_departure": "Moscow",
        "city_arrival": "Ярославль",
        "departure_times": 8.30,
        "travel_time": 3.25,
        "type_autos": "micro-bus"
    }


    response = requests.put(BASE_URL + "/route/10", data=json.dumps(new_route))


if __name__ == "__main__":
    pass

