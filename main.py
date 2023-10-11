import requests

api_key = "99d53ef0516223d7f1785a5342359e23"
LAT = 39.006699
LONG = -77.429131

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/weather"

#    "formatted": 0,
#
parameters = {
    "lat": 39.006699,
    "lon": -77.429131,
    "exclude": "current, minutely, daily, alerts",
    "appid": api_key,
}

response = requests.get(OWM_Endpoint, params=parameters)
response.raise_for_status()
data = response.json()
weather_data = data["weather"][0]["id"]

if weather_data < 700:
    print(f"It is going to rain, bring an umbrella")