from flask import Flask, render_template, request, redirect
from weatherForecastAPI import get_weather_data,display_weather

api_key = '5984a5ca308170ad88412364338705f2'
app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
        if request.method == 'GET':
                return render_template('index.html')
        #elif request.method == 'POST':
        #        if city == None:
        #                return render_template('index.html')
        else:
                city = request.form.get('city')
                print(city)
                data = get_weather_data(api_key=api_key, city=city)
                weatherParams = display_weather(data=data)

                name = weatherParams['city']
                country = weatherParams['country']
                temperature = weatherParams['temperature']
                feels_like = weatherParams['feels_like']
                description = weatherParams['description']
                humidity = weatherParams['humidity']
                wind_speed = weatherParams['wind_speed']

                weather = Weather(name.upper(),country,temperature,feels_like,description.upper(),humidity,wind_speed) 
                
                return render_template('forecast.html',weather = weather)

#@app.route('/weather_forecast', methods=['POST'])
#def weather_forecast():
#        if request.method == 'POST':
#                city = request.form.get('city')
#                print(city)
#                data = get_weather_data(api_key=api_key, city=city)
#                weatherParams = display_weather(data=data)
#
#                name = weatherParams['city']
#                country = weatherParams['country']
#                temperature = weatherParams['temperature']
#                feels_like = weatherParams['feels_like']
#                description = weatherParams['description']
#                humidity = weatherParams['humidity']
#                wind_speed = weatherParams['wind_speed']
#
#                weather = Weather(name,country,temperature,feels_like,description,humidity,wind_speed)
#
#                return render_template('index.html',weather = weather)

class Weather:
     def __init__(self,name,country,temperature,feels_like,description,humidity,wind_speed):
          self.name = name
          self.country = country
          self.temperature = temperature
          self.feels_like = feels_like
          self.description = description
          self.humidity = humidity
          self.wind_speed = wind_speed