import tkinter as tk
import requests
from tkinter import messagebox
from PIL import Image, ImageTk
import ttkbootstrap


#Function to get the wether information from OpenWatherMap API

def get_weather(city):
    #insert your api key from openweather map.com
    #form a new account and click on my apis
    API_key = ""
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}"
    res = requests.get(url)

    if res.status_code == 404:
        messagebox.showerror("Error", "City  not found")
        return None
    
    #parse the response jSON to get weather information

    weather = res.json()
    icon_id = weather['weather'][0]['icon']
    temperature = weather['main']['temp'] - 273.15
    description = weather['weather'][0]['description']
    city = weather['name']
    country = weather['sys']['country']

    #Get the icon url and return all the weather information

    icon_url = f"https://openweathermap.org/img/wn/{icon_id}@2x.png"
    return (icon_url, temperature, description, city, country)


#Function to search weather

def search():
    city = city_entry.get()
    result = get_weather(city)
    if result is None:
        return
    
    #if the city is found unpack the weather information
    icon_url, temperature, description, city, country = result
    location_label.configure(text=f"{city}, {country}")

    #Get the weather icon image from the url and uodate the icon label

    image = Image.open(requests.get(icon_url, stream=True).raw)
    icon = ImageTk.PhotoImage(image)
    icon_label.configure(image=icon)
    icon_label.image = icon

    #Update the temprature and description labels

    temperature_label.configure(text=f"Temperature: {temperature:.2f}°C")
    description_label.configure(text=f"Description: {description}")

root = ttkbootstrap. Window(themename = "morph")
root.title("Weather App")
root.geometry("400x400")
 #enntry width


city_entry = ttkbootstrap.Entry(root, font="Helvetica, 18")
city_entry.pack(pady=10)

#button widgget to search for the weather information

search_button = ttkbootstrap.Button(root, text="Search", command = search, bootstyle = "warning")
search_button.pack(pady=10)

#labeling thee widget to show the city

location_label = tk.Label(root, font="Helvetica, 25")
location_label.pack(pady= 20)

#label to show the weather icon

icon_label = tk.Label(root)
icon_label.pack()

#label to show the temprature
temperature_label = tk.Label(root, font="Helvetica, 20")
temperature_label.pack()

#label to show the weather description

description_label = tk.Label(root, font="Helvetica, 20" )
description_label.pack()

root.mainloop()