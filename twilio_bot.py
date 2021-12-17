import requests
import os
from twilio.rest import Client

API_KEY = os.environ["API_OWN"]
LAT = 19.432680
LONG = -99.134209
ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
account_sid = "ACd913eab39082ec0af0593f7f6f8a4252"
auth_token = os.environ["AUTH_TOKEN"]

parameters = {
    "lat": LAT,
    "lon": LONG,
    "appid": API_KEY,
    "exclude": "current,minutely,daily"
}

response = requests.get(url=ENDPOINT, params=parameters)
response.raise_for_status()
weather_data = response.json()["hourly"]
weather_slice = weather_data[:12]

will_rain = False

for weather in weather_slice:
    weather_hour = weather["weather"]
    for j in range(len(weather_hour)):
        weather_id = weather_hour[j]["id"]
        will_rain = True if weather_id < 700 else False

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="Trae una sombrilla perra, llovera hoy Ian puto",
        from_='+14582305585',
        to='+525538948420'
    )
    print(message.status)