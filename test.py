import csv
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Base URL for Jumia
base_url = 'https://www.jumia.co.ke'

# Function to get category URLs
def get_category_urls():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(base_url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    category_links = []
    categories = soup.find_all('a', class_='itm')
    
    for category in categories:
        link = category.get('href')
        if link and link.startswith('/'):
            category_links.append(base_url + link)
    
    return category_links
