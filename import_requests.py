import requests

def get_weather(city):
    api_key = " 3dd0839a18a47499d1ce6a2da5e02b7c"
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {'q':city, '   ':api_key, 'units':'metrics'}
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        print(f"City: {data['name']}")
        print(f"Temp: {data['main']['temp']} C")
        print(f"Weather: {data['weather'][0]['description']}")
    else:
        print("City not found")
        
city = input("Enter city name")
get_weather(city)

