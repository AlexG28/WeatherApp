from tkinter import *
import requests
import ApiKey





def updateCity():
    cityName = cityInput.get()
    data = WeatherReport(cityName)

    Label(window, text = (f"the temperature in {cityName} is {data['temperature']}"), bg='white', fg = 'black').grid(row=0, column=0,sticky=W)



def main():
    global window 
    window = Tk()
    window.title("Weather App")
    window.configure(background = "white")

    data = WeatherReport()

    Label(window, text = (f"the temperature in Toronto is {round(data['temperature'],2)}"), bg='white', fg = 'black').grid(row=0, column=0,sticky=W)
   
    global cityInput
    cityInput = Entry(window, width = 20, bg = "white")
    cityInput.grid(row=1, column = 0, sticky=W)

    Button(window, text = "Submit", width = 6, command = updateCity).grid(row = 3, column=1, sticky=W)

    

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

