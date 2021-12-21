import requests

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.put_endpoint = "https://api.sheety.co/99d6b6d87694b1f22311cec64442538f/flightDeals/prices"
        self.get_endpoint = "https://api.sheety.co/99d6b6d87694b1f22311cec64442538f/flightDeals/prices"
        self.cities = self.get_cities()
        self.row_city = {}

    def get_cities(self):
        # Get all cities in google sheet
        response = requests.get(url=self.get_endpoint)
        response.raise_for_status()
        data = response.json()["prices"]
        self.cities = [data[i]["city"] for i in range(len(data))]
        return self.cities

    def update_iata_codes(self, cities):
        # Update IATA codes in google sheet
        row = 2
        for city in cities:
            iata_config = {
                "price": {
                    "city": city,
                    "iataCode": cities[city]
                }
            }
            self.row_city[cities[city]] = row
            response = requests.put(url=f"{self.put_endpoint}/{row}", json=iata_config)
            row += 1
        return 0


    def is_cheaper(self, city: str, price: float):
        # Returns true if the price is cheaper
        response = requests.get(url=f"{self.get_endpoint}/{self.row_city[city]}")
        response.raise_for_status()
        city_price = response.json()["price"]["lowestPrice"]
        if price <= city_price:
            return True
        return False
        

