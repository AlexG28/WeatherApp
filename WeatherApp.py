from tkinter import *
import requests
import ApiKey




def updateCity():
    cityName = cityInput.get()

    if cityName == "":
        cityName = "Toronto"

    data = WeatherReport(cityName)
   
    textTemperature.set(f"The temperature in {cityName} is {data['temperature']}")
    textHumidity.set(f"The humidity in {cityName} is {data['humidity']}")
    textWindspeed.set(f"The windpseed in {cityName} is {data['windspeed']}")

    
    #os.chdir('C:\Users\Aleksandr\Documents\Python_Programming\WeatherApp')
    if data['main'] == 'Clouds':
        photo1.configure(file='weatherSymbols\\cloudy.png')
    elif data['main'] == 'Clear':
        photo1.configure(file='weatherSymbols\\sunny.png')
    elif data['main'] == 'Snow':
        photo1.configure(file='weatherSymbols\\snowy.png')
    else:
        photo1.configure(file='weatherSymbols\\raining.png')

    
    
    #photo1.configure(file='raining.png')
    
    

def main():
    global window 
    window = Tk()
    window.title("Weather App")
    window.configure(background = "white")

    global cityInput
    cityInput = Entry(window, width = 20, bg = "white")
    cityInput.grid(row=1, column = 0, sticky=W)
    
    global textTemperature
    textTemperature = StringVar()

    global textHumidity
    textHumidity = StringVar()

    global textWindspeed
    textWindspeed = StringVar()

    global photo1
    photo1 = PhotoImage()   
   

    #global photoLabel
    

    Label(window, text = "please enter the name of the City you want to search", bg = "white", fg = "black").grid(row=0,column=0,sticky=W)
    Button(window, text = "Submit", width = 6, command = updateCity).grid(row = 2, column=0, sticky=W) 

    Label(window, textvariable = textTemperature, bg='white', fg = 'black').grid(row=0, column=1,sticky=W)
    Label(window, textvariable = textHumidity, bg='white', fg = 'black').grid(row=1, column=1,sticky=W)
    Label(window, textvariable = textWindspeed, bg='white', fg = 'black').grid(row=2, column=1,sticky=W)

    Label(window, image = photo1).grid(row =0, column = 0, sticky=W)
    updateCity()


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

