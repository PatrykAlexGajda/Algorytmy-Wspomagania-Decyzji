import openmeteo_requests
import requests_cache
import pandas as pd

import matplotlib.pyplot as plt
from retry_requests import retry

# Klasa do przechowania wszystkiego istotnego dla pogody
# Potem bedzie lista 7 razy takie obiekty na kazdy dzien, ewentualnie rozbijemy drobniej na godziny to wtedy 24 * 7 lista tych obiektow
class WeatherData:
    def __init__(self, date="rrrr-mm-dd", localization="Wroclaw", rain_probability=0,
                 snow_probability=0, wind_speed=0, humidity=0, temperature=20,
                 uv_index=0, air_quality=0):
        
        self.date = date
        self.localization = localization
        self.rain_probability = rain_probability
        self.snow_probability = snow_probability
        self.wind_speed = wind_speed
        self.humidity = humidity
        self.temperature = temperature
        self.uv_index = uv_index
        self.air_quality = air_quality

    def showData(self):
        print(f"Date: {self.date}, Localization: {self.localization}")
        print(f"Rain probability: {self.rain_probability}")
        print(f"Snow probabilty: {self.snow_probability}")
        print(f"Wind speed: {self.wind_speed}")
        print(f"Humidity: {self.humidity}")
        print(f"Temperature: {self.temperature}")
        print(f"UV Index: {self.uv_index}")
        print(f"Air quality: {self.air_quality}")


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
        "hourly": "temperature_2m"
    }
    responses = session.weather_api(url, params=params)
    response = responses[0]

    return response

# Prognoza na tydzien co godzine
def hourlyForecast(response):
    hourly = response.Hourly()
    hourly_temperature_2m = hourly.Variables(0).ValuesAsNumpy()

    # To jest cos do wyswietlania ladniejsze, niepotrzebne potem raczej
    hourly_data = {"date": pd.date_range(
        start = pd.to_datetime(hourly.Time(), unit = "s", utc = True),
        end = pd.to_datetime(hourly.TimeEnd(), unit = "s", utc = True),
        freq = pd.Timedelta(seconds = hourly.Interval()),
        inclusive = "left"
    )}

    # Dodanie temperature_2m (w sensie na 2 metrach) do wyswietlania
    hourly_data["temperature_2m"] = hourly_temperature_2m
    hourly_dataframe = pd.DataFrame(data = hourly_data)

    return hourly_temperature_2m
    

session = createSession()
response = getApiResponse(session)
week_temperature = hourlyForecast(response)

week_forecast = [] 

for i in range(7):
    day_forecast = WeatherData(temperature=week_temperature[12*(i+1)])
    week_forecast.append(day_forecast)

for day in week_forecast:
    day.showData()
    print("\n")