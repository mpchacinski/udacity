import requests

status_code = 0

while status_code != 200:
    city = input("Where in the world are you? ")

    link = (f"http://api.openweathermap.org/data/2.5/weather?q={city}"
            "&APPID=a20b19225e481c25767778b6203c1ab8&units=metric")

    r = requests.get(link)
    status_code = r.status_code
    if status_code == 404:
        print("No such city, try again!")
    json_weather = r.json()


def display_weather(city, state, temp, pressure, country):
    print(f"The weather in {city.capitalize()}, {country}:")
    print(f"State:\t{state}")
    print(f"Temperature :\t{temp}")
    print(f"Pressure :\t{pressure}")


state = json_weather["weather"][0]["description"]
temp = json_weather["main"]["temp"]
pressure = json_weather["main"]["pressure"]
country = json_weather["sys"]["country"]

display_weather(city, state, temp, pressure, country)
