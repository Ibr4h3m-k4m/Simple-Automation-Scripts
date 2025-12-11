import requests

API_KEY ="REDACTED"
API_LINK = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter The city name of which you wanna know the current weather: ")

request_url = f"{API_LINK}?appid={API_KEY}&q={city}"
response = requests.get(request_url)


if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]["description"]
    tempurate = data["main"]["temp"] - 273.15
    print(f"The current weather in {city} is {weather} with a temperature of {tempurate:.2f}°C")
else:
    print("An Error has occured, please check your internet connexion or notify the admin")
    
