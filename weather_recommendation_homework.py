import logging.config
import requests
from logging_configuration_homework import LOGGING_CONFIG

def setup_logging():
    logging.config.dictConfig(LOGGING_CONFIG)

def fetch_weather_data(location):
    url = 'https://api.tomorrow.io/v4/weather/forecast?location=42.3478,-71.0466&apikey=qIisEX1bC3Y3NDnHsDIIkpma0SbBEHhN'
    querystring = {
        "location": location,
        "fields": ["temperature", "precipitationType"],
        "units": "imperial",
        "timesteps": "1d"
    }

    try:
        response = requests.get(url, params=querystring)
        if response.status_code == 200:
            logging.info("Important: API call is successful")
            weather_data = response.json()
            return weather_data
        else:
            logging.error(f"API call failed with status code: {response.status_code}")

    except Exception as e:
        logging.critical(f"An unexpected error occurred: {e}")

def recommend_activities(weather_data):
    if not weather_data:
        logging.info("The data is missing")

    try:
        day_data = weather_data['timelines']['daily'][0]['values']
        precipitation_probability_avg = day_data['precipitationProbabilityAvg']
        wind_speed_avg = day_data['windSpeedAvg']
        cloud_cover_avg = day_data['cloudCoverAvg']
        if precipitation_probability_avg > 3:
            return "It looks like rainy. Let's visit a museum or enjoy a good book at home."
        elif wind_speed_avg > 7:
            return "It's windy! Let's not go for hiking or a picnic in the park."
        elif cloud_cover_avg > 50:
            return "It's cold. Let's visit an indoor pool."
        else:
            return "It's a nice day. Let's ride a bicycle."
    except KeyError as e:
        logging.error(f"Important: Missing key in weather data: {e}")
        return "No suggestion because of no data."

setup_logging()
logging.info("Important: Weather-Based Activity Recommender started")
location = "40.0691, 45.0382"
try:
    weather_data = fetch_weather_data(location)
    activities = recommend_activities(weather_data)
    print(f"Recommended activities based on current weather: {activities}")
except Exception as e:
    logging.critical(f"An error occurred: {e}")
