from tkinter import *
import requests



def main():
    return 
    #used for GUI and such


def WeatherReport(cityName = "Toronto", key = "1a6e299186e76c80b2ff984ceebf2725"):

    response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={cityName}&units=metric&appid={key}")
    weatherReport = response.json()
    return weatherReport #returns the weather report in a json format




