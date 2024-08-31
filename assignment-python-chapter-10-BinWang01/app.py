# Bin Wang
import requests

# Chapter 10.2- Pip
response = requests.get("http://google.com")
print(response)
print(response.url)
print(response.text)
