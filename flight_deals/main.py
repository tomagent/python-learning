#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch

data_manager = DataManager()

flight_data = FlightData(data_manager.cities)
codes = flight_data.get_iata_codes()
data_manager.update_iata_codes(codes)

codes_lst = list(codes.values())
for city in codes_lst:
    flight_search = FlightSearch(city)
    price = flight_search.search_flight()
    if data_manager.is_cheaper(city, price):
        flight_search.send_sms()

