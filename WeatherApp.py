from tkinter import *
import requests
import ApiKey


def main():
    window = Tk()
    window.title("Weather App")
    window.configure(background = "white")

    data = WeatherReport()

    Label(window, text = (f"the temperature is {data['temperature']}"), bg='white', fg = 'black').grid(row=1, column=1,sticky=W)
    
    window.mainloop()

    


def WeatherReport(cityName = "Toronto", key = ApiKey.key()):

    response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={cityName}&units=metric&appid={key}")
    weatherReport = response.json()
    #returns the weather report in a json format

    outputDict = {}
    

    outputDict['main'] = weatherReport['weather'][0]['main']
    outputDict['temperature'] = weatherReport['main']['temp']
    outputDict['humidity'] = weatherReport['main']['humidity']
    outputDict['windspeed'] = weatherReport['wind']['speed']
    outputDict['wind direction'] = weatherReport['wind']['deg']

    return outputDict

   


main()

