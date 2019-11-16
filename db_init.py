
import sqlite3
import random

DB_PATH = 'db.sqlite3'

def init():
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    cursor.executescript(open('shema.sql', 'r').read())
    connection.commit()
    connection.close()


trade_names = [
    "Белая березка",
    "Рябинка",
    "Большой бродяга",
    "Малый бродяга",
    "Аист",
    "Мохнатый шмель"
]

city_departure = ['Moscow']

city_arrivals = [
    "Калуга",
    "Ступино",
    "Ростов-на-Дону",
    "Симферополь",
    "Брянск"
]
departure_times = [9.28, 10.35, 12.45, 16.10, 19.21, 21.08]

travel_time = {
    "Калуга": 2.55,
    "Ступино": 1.45,
    "Ростов-на-Дону": 20.12,
    "Симферополь": 36.20,
    "Брянск": 8.15
}


type_autos = ["bus", "micro-bus", "taxi"]

def next_route():
        trade_name = random.choice(trade_names)
        departure_time = random.choice(departure_times)

        return trade_name, departure_time




def check_table(): #cant be normally reached
    connection = sqlite3.connect(DB_PATH)
    c = connection.cursor()
    cmd = "SELECT * FROM routes"
    c.execute(cmd)
    r = c.fetchall()
    for i in r:
        print(i)

    c.execute(cmd)
    connection.commit()
    connection.close()




if __name__ == "__main__":
    init()
    #make_data()
    check_table()
