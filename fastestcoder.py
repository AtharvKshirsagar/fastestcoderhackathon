import requests
import json

def get_weather(city_name):
    api_key = '41544a34c1f1007413feb77f68ff1168'  # Replace with your OpenWeatherMap API key
    base_url = 'http://api.openweathermap.org/data/2.5/weather'

    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric'
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise an exception for any HTTP errors

        weather_data = response.json()

        # Parse the weather data
        temperature = weather_data['main']['temp']
        description = weather_data['weather'][0]['description']

        # Print the weather forecast
        print(f"Temperature: {temperature}°C")
        print(f"Description: {description}")
    
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as err:
        print(f"Error occurred: {err}")
    except KeyError as key_err:
        print(f"Error parsing weather data: {key_err}")
    except json.JSONDecodeError as json_err:
        print(f"Error decoding JSON response: {json_err}")

if __name__ == '__main__':
    city = input("Enter a city name: ")
    get_weather(city)
