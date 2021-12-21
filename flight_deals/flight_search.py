from datetime import datetime, timedelta
import requests
from notification_manager import NotificationManager

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self, destination: str):
        self.api_key = "aWQJr_21cr8jMzClvASarZUNgyeXBkJ2"
        self.api_endpoint = "https://tequila-api.kiwi.com/v2/search"
        self.home = "LON"
        self.destination = destination
        self.today = datetime.now().today().date()
        self.tomorrow = self.today + timedelta(days=1)
        self.date_six_months = self.tomorrow + timedelta(days=180)
        self.tomorrow = self.tomorrow.strftime("%d/%m/%Y")
        self.date_six_months = self.date_six_months.strftime("%d/%m/%Y")

    def search_flight(self):
        self.header = {
            "apikey": self.api_key
        }
        flight_config = {
            "fly_from": self.home,
            "fly_to": f"city:{self.destination}",
            "date_from": self.tomorrow,
            "date_to": self.date_six_months,
            "nights_in_dst_from": 3,
            "nights_in_dst_to": 14,
            "flight_type": "round",
            "curr": "GBP",
            "sort": "price",
        }
        response = requests.get(url=self.api_endpoint, headers=self.header, params=flight_config)
        response.raise_for_status()
        data = response.json()["data"][0]
        self.price = float(data["price"])
        self.origin_city = data["route"][0]["cityFrom"]
        self.origin_airport = data["route"][0]["flyFrom"]
        self.destination_city = data["route"][0]["cityTo"]
        self.destination_airport = data["route"][0]["flyTo"]
        self.leave_date = data["route"][0]["local_departure"].split("T")[0]
        self.return_date = data["route"][1]["local_departure"].split("T")[0]
        self.airline = data["route"][0]["airline"]
        return self.price

    def send_sms(self):
        NotificationManager(self.origin_city, self.origin_airport, self.destination_city, self.destination_airport,
                            self.leave_date, self.return_date, self.airline, self.price)