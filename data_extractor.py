"""Internal imports"""

import requests
from ow_api import API_KEY

class DataExtractor:
    
    @staticmethod
    def get_ow_data(city_name):
        
        """
        Return the json datas of the place from OpenWeather API

            Parameter
            ----------
            city_name : type str
                The name of the location.
        """

        ow_base_url = "https://api.openweathermap.org/data/2.5/weather?q="
        ow_api_url = ow_base_url + city_name + "&appid=" + API_KEY + "&lang=fr"
        response = requests.get(ow_api_url)
        data = response.json()

        response_code = data['cod']
        if response_code == 200:
            city_name = data['name']
            country = data['sys']['country']
            description = data['weather'][0]['description']
            humidity = data['main']['humidity']
            temperature_kelvin = data['main']['temp']
            temperature_celsius = int(round(temperature_kelvin, 0) - 273.15)
            wind_speed = int(round(data['wind']['speed'] * 3,11))
            icon_code = data['weather'][0]['icon']
            weather_icon = "http://openweathermap.org/img/w/" + icon_code + ".png"
            
            response = {
                "city_name": city_name,
                "country": country,
                "description": description,
                "humidity": humidity,
                "temperature": temperature_celsius,
                "wind_speed": wind_speed,
                "weather_icon": weather_icon,
                "response_code":response_code
            }        
        else:
            response = {
                "response_code": response_code,
                "message": "Nom inconnu"
                }
        return response
