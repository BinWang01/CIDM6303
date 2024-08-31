import requests
"""
Documentation at
https://documenter.getpostman.com/view/10808728/SzS8rjbc
"""

# 1. get the API data from the web server
# This API server does not require an API key
# 2. Convert the data into a useful python objects: usually a list or dictionaries
url = "https://api.covid19api.com/summary"


# Bin Wang
# Get data from Yelp using API calls
# Need to watch Mosh' video 10.4 AND 10.5 to understand this code.
# Dr. Humpherys added different ways to filter and loop through the data


response = requests.get(url)
result = response.json()
global_data = result["Global"]

total_deaths = global_data['TotalDeaths']
total_confirmed = global_data['TotalConfirmed']
mortality_rate = total_deaths/total_confirmed
print(
    f"Total Deaths: {total_deaths}\nTotal Confirmed Cases: {total_confirmed}\nMortality Rate: {mortality_rate:.3f}")
