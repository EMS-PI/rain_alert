import requests
from twilio.rest import Client
import os

VERBOSE = os.environ["VERBOSE"]

OWM_URL = "https://api.openweathermap.org/data/3.0/onecall"
LATITUDE = os.environ["LATITUDE"]
LONGITUDE = os.environ["LONGITUDE"]
TIWILIO_ACCOUNT_SID = os.environ["TIWILIO_ACCOUNT_SID"]

if VERBOSE:
    print(f"Request weather data for latitude {LATITUDE} and longitude {LONGITUDE}")

params = {
    "lat": LATITUDE,
    "lon": LONGITUDE,
    "appid": os.environ["OWM_API_KEY"],
    "exclude": "current,minutely,daily",
    "units": "imperial"
}

response = requests.get(OWM_URL,params=params)
response.raise_for_status()
data = response.json()

weather_next_12h = data["hourly"][:12]
condition_id = [weather_h["weather"][0]["id"] for weather_h in weather_next_12h]

rain_today = False
for idx in range(0,12):
    if data["hourly"][idx]["weather"][0]["id"] < 600:
        rain_today = True

if rain_today:
    auth_token = os.environ["TWILIO_AUTH_TOKEN"]
    client = Client(TIWILIO_ACCOUNT_SID, auth_token)
    message = client.messages.create(
      body="It is going to rain today. Bring an umbrella ☂️",
      from_=os.environ["FROM_NUMBER"],
      to=os.environ["TO_NUMBER"]
    )
    print(message.status)
else:
    if VERBOSE:
        print("No rain today.")
