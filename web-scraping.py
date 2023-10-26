# Python script for web scraping to extract data from a website
import requests
from bs4 import BeautifulSoup
def scrape_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
# Your code here to extract relevant data from the website
