import requests

# Load and clean API key
api_key = open('api_key.txt', 'r').read().replace(' ', '').replace('\n', '').strip()

# Input location
location = input("Location: ")

# Get weather
url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&units=metric&appid={api_key}"
result = requests.get(url)

if result.status_code == 200:
    data = result.json()
    temp = data['main']['temp']
    condition = data['weather'][0]['main']

    print(f"Weather in {location}: {condition}, {temp}°C")

    # Clothing suggestion
    def suggest_clothing(temp, condition):
        suggestion = ""
        if temp < 0:
            suggestion = "Heavy coat, gloves, scarf"
        elif 0 <= temp <= 10:
            suggestion = "Jacket, sweater, long pants"
        elif 11 <= temp <= 20:
            suggestion = "Light jacket, long sleeves"
        elif 21 <= temp <= 30:
            suggestion = "T-shirt, shorts"
        else:
            suggestion = "Light clothing, hat, sunglasses"

        if condition.lower() in ['rain', 'snow']:
            suggestion += " + waterproof jacket or umbrella"
        return suggestion

    print("Suggested clothing:", suggest_clothing(temp, condition))

else:
    print("Error:", result.status_code, result.json())

