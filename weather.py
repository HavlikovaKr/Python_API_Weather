import requests

api_key = '30d4741c779ba94c470ca1f63045390a' 
city = input("Enter city: ")

response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}")

if response.status_code == 404:
    print("No city found. Please check the city name and try again.")
else:
    data = response.json()

    main = data["weather"][0]["main"]
    description = data["weather"][0]["description"]

    print(f"Current weather in {city} is {main}.")
    print(f"Current visibility in {city} is {description}.")



 
