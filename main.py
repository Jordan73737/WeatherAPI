import requests

api_key = '60d34a9d00d5cb10f9bf5f9d7af21ef0'

user_input = input("Enter city: ")

weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

if weather_data.json()['cod'] == '404':
    print("No City Found")
else:
    weather = weather_data.json()['weather'][0]['main']
    temp = round((weather_data.json()['main']['temp'] - 32) * (5 / 9))
    humidity = weather_data.json()['main']['humidity']
    wind_speed = weather_data.json()['wind']['speed']


    print(f"The Weather in {user_input} is: {weather}")
    print(f"The Temperature in {user_input} is: {temp}ºC")
    print(f"The Humidity in {user_input} is {humidity}%")
    print(f"The Wind speed in {user_input} is {wind_speed}kmph")

#print(weather_data.json())

