import requests

class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self, cities):
        self.url = "https://tequila-api.kiwi.com/"
        self.api_key = "aWQJr_21cr8jMzClvASarZUNgyeXBkJ2"
        self.cities = cities
        self.codes = {}

    def get_iata_codes(self):
        for city in self.cities:
            header = {
                "apikey": self.api_key,
            }
            parameters = {
                "term": city,
                "location_types": "city"
            }

            response = requests.get(url=f"{self.url}locations/query", params=parameters, headers=header)
            response.raise_for_status()
            data = response.json()
            code = data["locations"][0]["code"]
            self.codes[city] = code
        return self.codes
