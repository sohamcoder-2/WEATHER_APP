import requests
from dotenv import load_dotenv
import os
from dataclasses import dataclass

load_dotenv()
api_key=os.getenv('apikey')

@dataclass
class WeatherData:
    main:str
    description:str
    icon:str
    temp:float


def get_info(city_name,state_code,country_code,API_key):
    resp=requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&appid={API_key}').json()
    data=resp[0]
    lat,lon=data.get('lat'),data.get('lon')
    return lat,lon


def get_weather_info(lat,lon,API_key):
    resp=requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}&units=metric').json()
    data=WeatherData(
        main=resp.get('weather')[0].get('main'),
        description=resp.get('weather')[0].get('description'),\
        icon=resp.get('weather')[0].get('icon'),
        temp=resp.get('main').get('temp')

    )
    return data

def main(city_name,state_code,country_code):
    lat, lon = get_info(city_name, state_code, country_code, api_key)
    weather_data=get_weather_info(lat,lon,api_key)
    return weather_data

if __name__=="__main__":
    # g=get_info('Toronto','ON','Canada',api_key)
    # print(g)
    lat,lon=get_info('Toronto','ON','Canada',api_key)
    w=get_weather_info(lat,lon,api_key)
    print(w)