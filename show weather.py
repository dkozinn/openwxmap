#!/usr/bin/env python3
# pylint: disable=invalid-name, line-too-long
# flake8: noqa

'''
Simple command line script to show current weather
'''

import json
import os
import sys
from time import localtime, strftime

import requests

# Get the API key from the environment variable

API_KEY = os.environ["WEATHER_API_KEY"]

DEFAULT_CITY = "River Vale"
UNITS = "imperial"

if len(sys.argv)>1:
    city = ' '.join(sys.argv[1:]).title()
else:
    city = DEFAULT_CITY


GEO_URL = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={API_KEY}"
#print(URL)
#print(f"City = {CITY}")

def degrees_to_cardinal(degree):
    '''
    note: this is highly approximate...
    '''
    dirs = ["North", "North-NorthEast", "NorthEast", "East-NorthEast", "East", "East-SouthEast", "SouthEast", "South-SouthEast",
            "South", "South-SouthWest", "SouthWest", "West-SouthWest", "West", "West-NorthWest", "NorthWest", "North-NorthWest"]
    i = int((degree + 11.25)/22.5)
    return dirs[i % 16]

def to_localtime(when):
    '''
    Convert epoch time to human-readable
    '''
    return strftime('%H:%M:%S', localtime(when))

# Get lat & long

response = requests.get(GEO_URL, timeout=15)
geo = json.loads(response.content)
try:
    LAT = geo[0]['lat']
    LON = geo[0]['lon']
    CITY = geo[0]['name']
    STATE = geo[0]['state']
    COUNTRY = geo[0]['country']
except IndexError:
    sys.exit(f"Unable to find city \"{city}\"")

# Make a request to the weather API

WX_URL = f"https://api.openweathermap.org/data/2.5/weather?lat={LAT}&lon={LON}&appid={API_KEY}&units={UNITS}"
FORECAST_URL = f"https://api.openweathermap.org/data/2.5/forecast?lat={LAT}&lon={LON}&appid={API_KEY}&units={UNITS}"
#print(URL)
response = requests.get(WX_URL, timeout=15)

# Check if the request was successful
if response.status_code == 200:
    # Get the weather data from the response
    data = json.loads(response.content)

    # Print the weather report to the console
    print(f"Weather for {CITY}, {STATE} {COUNTRY}:")
    print(f"Description: {data['weather'][0]['description']}")
    print(f'Temperature: {(data["main"]["temp"])}°F')
    print(f'Feels like: {(data["main"]["feels_like"])}°F')

    print(f"Humidity: {data['main']['humidity']}%")
    print(f"Wind {data['wind']['speed']} mph from the {degrees_to_cardinal(data['wind']['deg'])}", end='')
    if "gust" in data['wind']:
        print(f" with gusts to {data['wind']['gust']} mph", end='')
    print(f"\nSunrise: {to_localtime(data['sys']['sunrise'])} / Sunset: {to_localtime(data['sys']['sunset'])}")
else:
    # The request was not successful
    print("Error fetching weather data.")

#FORECAST_URL = f"https://api.openweathermap.org/data/2.5/forecast?lat={LAT}&lon={LON}&appid={API_KEY}&units={UNITS}"
#print(URL)
forecast_response = requests.get(FORECAST_URL, timeout=15)

# Check if the request was successful
# if response.status_code == 200:
#     # Get the weather data from the response
#     data = json.loads(forecast_response.content)
# else:
#     print("Error fetching forecast data.")
