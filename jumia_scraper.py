import requests
from bs4 import BeautifulSoup
import pandas as pd

# Jumia category URLs (you can expand this list)
urls = [
    'https://www.jumia.co.ke/appliances/',
    'https://www.jumia.co.ke/home-office/',
    'https://www.jumia.co.ke/fashion/',
    'https://www.jumia.co.ke/computing/',
    'https://www.jumia.co.ke/supermarket/'
]

# Function to scrape discount products from a given category URL
def scrape_discount_products(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    products = soup.find_all('article', class_='prd _fb col c-prd')
    product_list = []
    
    for product in products:
        name = product.find('h3', class_='name').text.strip()
        price = product.find('div', class_='prc').text.strip()
        discount = product.find('div', class_='bdg _dsct _sm')
        discount_text = discount.text.strip() if discount else 'No discount'
        
        product_list.append({
            'Name': name,
            'Price': price,
            'Discount': discount_text
        })
    
    return product_list

# Scrape data from all URLs
all_products = []
for url in urls:
    products = scrape_discount_products(url)
    all_products.extend(products)

# Convert to DataFrame and save to CSV
df = pd.DataFrame(all_products)
df.to_csv('jumia_discount_products.csv', index=False)

print("Scraping completed and data saved to 'jumia_discount_products.csv'")
