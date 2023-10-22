import requests


city = input("Where in the world are you? ")

link = (f"http://api.openweathermap.org/data/2.5/weather?q={city}"
        "&APPID=a20b19225e481c25767778b6203c1ab8&units=metric")

r = requests.get(link)
json_weather = r.json()

state = json_weather["weather"][0]["description"]
temp = json_weather["main"]["temp"]
pressure = json_weather["main"]["pressure"]

print(f"The weather in {city}:")
print(f"State:\t{state}")
print(f"Temperature :\t{temp}")
print(f"Pressure :\t{pressure}")
