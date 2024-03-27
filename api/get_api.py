import openmeteo_requests
import requests_cache
import pandas as pd
import datetime

import matplotlib.pyplot as plt
from retry_requests import retry

# Klasa do przechowania wszystkiego istotnego dla pogody
# Potem bedzie lista 7 razy takie obiekty na kazdy dzien, ewentualnie rozbijemy drobniej na godziny to wtedy 24 * 7 lista tych obiektow
class WeatherData:
    def __init__(self, date=None, hour=None, localization="Wroclaw", precipitation_probability=0,
                 cloud_cover=0, visibility=0, wind_speed=0, humidity=0, temperature=20,
                 uv_index=0, is_day=False):
        
        self.date = date
        self.hour = hour
        self.localization = localization
        self.temperature = temperature
        self.humidity = humidity
        self.precipitation_probability = precipitation_probability
        self.cloud_cover = cloud_cover
        self.visibility = visibility
        self.wind_speed = wind_speed
        self.uv_index = uv_index
        self.is_day = is_day

    def showData(self):
        print(f"Date: {self.date.day}.{self.date.month}.{self.date.year} {self.hour}, Localization: {self.localization}")
        print(f"Precipitation probability: {self.precipitation_probability} %")
        print(f"Cloud cover: {self.cloud_cover} %")
        print(f"Visibility: {self.visibility} m")
        print(f"Wind speed: {self.wind_speed} km/h")
        print(f"Humidity: {self.humidity} %")
        print(f"Temperature: {self.temperature} celsius")
        print(f"UV Index: {self.uv_index} mW/m^2")
        print(f"Is Day: {self.is_day}")


# Otwieranie sesji, powtorzenia i cache z jakiegos powodu xd
def createSession():
    cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
    retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
    openmeteo = openmeteo_requests.Client(session = retry_session)

    return openmeteo

def getApiResponse(session):
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": 51.107883,
        "longitude": 17.038538,
        "hourly": ["temperature_2m", "relative_humidity_2m", "precipitation_probability", 
                   "cloud_cover", "visibility", "wind_speed_10m", "uv_index", "is_day"]
    }
    responses = session.weather_api(url, params=params)
    response = responses[0]


    return response

# Prognoza na tydzien co godzine
def hourlyForecast(response):
    hourly = response.Hourly()
    hourly_temperature_2m = hourly.Variables(0).ValuesAsNumpy()
    hourly_relative_humidity_2m = hourly.Variables(1).ValuesAsNumpy()
    hourly_precipitation_probability = hourly.Variables(2).ValuesAsNumpy()
    hourly_cloud_cover = hourly.Variables(3).ValuesAsNumpy()
    hourly_visibility = hourly.Variables(4).ValuesAsNumpy()
    hourly_wind_speed_10m = hourly.Variables(5).ValuesAsNumpy()
    hourly_uv_index = hourly.Variables(6).ValuesAsNumpy()
    hourly_is_day = hourly.Variables(7).ValuesAsNumpy()

    # To jest cos do wyswietlania ladniejsze, niepotrzebne potem raczej
    hourly_data = {"date": pd.date_range(
	start = pd.to_datetime(hourly.Time(), unit = "s", utc = True),
	end = pd.to_datetime(hourly.TimeEnd(), unit = "s", utc = True),
	freq = pd.Timedelta(seconds = hourly.Interval()),
	inclusive = "left"
    )}

    hourly_data["temperature_2m"] = hourly_temperature_2m
    hourly_data["relative_humidity_2m"] = hourly_relative_humidity_2m
    hourly_data["precipitation_probability"] = hourly_precipitation_probability
    hourly_data["cloud_cover"] = hourly_cloud_cover
    hourly_data["visibility"] = hourly_visibility
    hourly_data["wind_speed_10m"] = hourly_wind_speed_10m
    hourly_data["uv_index"] = hourly_uv_index
    hourly_data["is_day"] = hourly_is_day

    hourly_dataframe = pd.DataFrame(data = hourly_data)

    # print(hourly_dataframe.loc[0]["date"])

    return hourly_dataframe
    

session = createSession()
response = getApiResponse(session)
week_dataframe  = hourlyForecast(response)

week_forecast = [] 

for i in range(7):
    day_and_hour = 24*(i)
    hour = week_dataframe.loc[i]["date"].hour

    day_forecast = WeatherData(date=week_dataframe.loc[i]["date"],
                               hour=hour,
                               temperature=week_dataframe.loc[i]["temperature_2m"], 
                               humidity=week_dataframe.loc[i]["relative_humidity_2m"],
                               precipitation_probability=week_dataframe.loc[i]["precipitation_probability"],
                               cloud_cover=week_dataframe.loc[i]["cloud_cover"],
                               visibility=week_dataframe.loc[i]["visibility"],
                               wind_speed=week_dataframe.loc[i]["wind_speed_10m"],
                               uv_index=week_dataframe.loc[i]["uv_index"],
                               is_day=week_dataframe.loc[i]["is_day"])
    
    week_forecast.append(day_forecast)

for day in week_forecast:
    day.showData()
    print("\n")