import requests
import streamlit as st

API_KEY = "a6f81aff8e354cf14db2c448cbb27e5c"  # Your OpenWeatherMap API key
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    response = requests.get(BASE_URL, params=params)
    return response.json()

def main():
    st.title("Simple Weather App")

    city = st.text_input("Enter city name")

    if city:
        if st.button("Get Weather"):
            data = get_weather(city)

            if data.get("cod") == 200:
                st.success(f"Weather in {data['name']}, {data['sys']['country']}")
                st.write(f"🌡️ Temperature: {data['main']['temp']}°C")
                st.write(f"💧 Humidity: {data['main']['humidity']}%")
                st.write(f"🌥️ Condition: {data['weather'][0]['description'].capitalize()}")
                icon_code = data['weather'][0]['icon']
                icon_url = f"http://openweathermap.org/img/wn/{icon_code}@2x.png"
                st.image(icon_url)
            else:
                st.error("City not found. Please check the name and try again.")

if __name__ == "__main__":
    main()
