# if you want scrap a website
#install requests
#install bs4 as beautifulsoup
#install pandas as pd
#install streamlit as st
#install html5lib


import requests
from bs4 import BeautifulSoup
import pandas as pd
import streamlit as st
import html5lib
st.title("Weather Dashboard")
city_name = st.text_input("Enter City Name")

if st.button("Get Weather"):
    # Call the scrape_weather_data function
    # weather_data = scrape_weather_data([city_name])
    #st.write(weather_data)
# def scrape_weather_data(city):


# Weather.com URL
#URL = "https://weather.com"

# Cities to scrape
 CITIES = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]
 print(CITIES)
def scrape_weather_data(cities):
    weather_data = []
    for city in cities:
        city_url = f"{"URL"}/weather/today/l/{city}"
        response = requests.get(city_url)
        soup = BeautifulSoup(response.content, 'html.parser')
        print(city_url)
        print(response)
        print(soup)

        # Extract city name, temperature, and weather condition
        city_name = soup.find('h1', class_='location').text.strip()
        temperature = soup.find('div', class_='temp').text.strip()
        weather_condition = soup.find('div', class_='condition').text.strip()
        print(city_name)
        print(temperature)
        print(weather_condition)

        weather_data.append({
            'City': city_name,
            'Temperature': temperature,
            'Weather Condition': weather_condition
        })
    
    return pd.DataFrame(weather_data)

# Scrape weather data
weather_df = scrape_weather_data(CITIES)
print(weather_df)

#Streamlit App
st.title("Weather Dashboard")
st.write("Search for a city or sort by temperature:")

# Search bar
search_city = st.text_input("Search City")
print(search_city)


# Sort by temperature
sort_temp = st.checkbox("Sort by Temperature")
print(sort_temp)

if sort_temp:
    weather_df = weather_df.sort_values(by='Temperature')
print(weather_df)

# Display weather data
st.write(weather_df)

# Filter by search city
if search_city:
    filtered_df = weather_df[weather_df['City'].str.contains(search_city, case=False)]
    st.write(filtered_df)
print(filtered_df)