import requests
import os
from twilio.rest import Client


# Log on to weather map, or sign up if you don't have an account
weather_map_endpoint = "https://api.openweathermap.org/data/2.5/onecall"
one_call_api = os.environ.get("WME_api")

# Go on twilio.com, sign up for an account.
# Generate your own account_sid and auth_token and replace it with the one below
account_sid = "My account_sid"
auth_token = os.environ.get("AUTH_TOKEN")

parameter = {
    "lat": ["Your location latitude"],
    "lon": ["Your location longitude"],
    "appid": one_call_api,
    "exclude": "current,minutely,daily"
}

response = requests.get(weather_map_endpoint, params=parameter)
response.raise_for_status()
weather_data = response.json()

# Get the weather id for the next 12 hours
weather_slice = weather_data["hourly"][:12]

will_rain = False

for each_weather in weather_slice:
    condition_code = each_weather["weather"][0]["id"]
    if int(condition_code) > 700:
        will_rain = True

if will_rain:
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an Umbrella ☔",
        from_="get this from the number generated on the twilio.com",
        to="replace with the number you signed up with on twilio.com"
    )
    print(message.status)