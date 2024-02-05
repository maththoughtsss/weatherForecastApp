import requests
import json

def get_weather_data(api_key, city):
    base_url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {
        'q' : city,
        'appid' : api_key,
        'units' : 'metric'
    }
    response = requests.get(base_url, params=params)
    data = response.json()
    return data

def display_weather(data):
    if data['cod'] != '404':
        city =  data['name']
        country = data['sys']['country']
        temperature = data['main']['temp']
        feels_like = data['main']['feels_like']
        description = data['weather'][0]['description']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']

        dict_data = {'city' : city,
                     'country' : country,
                     'temperature' : temperature,
                     'feels_like' : feels_like,
                     'description' : description,
                     'humidity' : humidity,
                     'wind_speed' : wind_speed
                     }

        print(f'Weather in {city}, {country}:')
        print(f'Temperature: {temperature}°C')
        print(f'Feels Like: {feels_like}°C')
        print(f'Description: {description}')
        print(f'Humidity: {humidity}%')
        print(f'Wind Speed: {wind_speed} km/h')

        #print(dict_data)
        return dict_data
    else:
        print('City not found. Please try again.')

def main():
    api_key = 'abd23b286f03966fff12f8a4c0bf273b'
    city = input('Enter the city name: ')
    weather_data = get_weather_data(api_key,city)
    display_weather(weather_data)

if __name__ == '__main__':
    main()