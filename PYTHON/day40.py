import requests
from bs4 import BeautifulSoup

city = input("Enter city name: ")

url = f"https://www.google.com/search?q=weather+{city}"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

try:
    temperature = soup.find("span", {"id": "wob_tm"}).text
    condition = soup.find("span", {"id": "wob_dc"}).text
    humidity = soup.find("span", {"id": "wob_hm"}).text

    print(f"\nWeather in {city}:")
    print(f"Temperature: {temperature}°C")
    print(f"Condition: {condition}")
    print(f"Humidity: {humidity}")

except:
    print("Could not fetch weather. Try another city.")