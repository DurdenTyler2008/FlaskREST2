
from flask import Flask
from flask import request
import sqlite3
import json


PATH_DB = "db.sqlite3"

app = Flask(__name__)


@app.route("/api/routes", methods=["GET"])
def all_routes():

    route_filter = request.args.get('route')

    connection = sqlite3.connect(PATH_DB)
    c = connection.cursor()

    if not route_filter:

        cmd = """
        SELECT id, trade_name, city_arrival, departure_time, type_auto FROM routes;
        """


    routes = c.fetchall()

    return json.dumps({"routes": routes})

    c.execute(cmd)
    connection.commit()
    connection.close()

    return "{}"


if __name__ == "__main__":
    app.run()