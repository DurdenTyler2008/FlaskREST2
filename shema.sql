
# РАСПИСАНИЕ МЕЖДУГОРОДНЫХ МАРШРУТОВ
# SCHEDULE OF LONG-DISTANCE ROUTES

DROP TABLE IF EXISTS routes;

CREATE TABLE routes(
	id INTEGER,
	trade_name VARCHAR,
	city_departure VARCHAR,
	city_arrival VARCHAR,
	departure_time INTEGER,
	travel_time INTEGER,
	type_auto VARCHAR,
	information VARCHAR

);
# trade_name фирм.название маршрута
# type_auto VARCHAR,# bus/micro-bus/taxi