from bs4 import BeautifulSoup
import requests
import pandas as pd

# Function to scrape product details
def scrape_product_details(url, headers):
    webpage = requests.get(url, headers=headers)
    soup = BeautifulSoup(webpage.content, "html.parser")
    
    # Find all product links
    links = soup.find_all("a", attrs={'class': 'a-link-normal s-no-outline'})
    product_links = []
    
    # Extract product links
    for link in links:
        href = link.get('href')
        if href.startswith('/'):
            product_links.append("https://www.amazon.com" + href)
    
    # Initialize lists to store data
    names = []
    prices = []
    ratings = []
    
    # Iterate through each product link
    for product_link in product_links:
        new_webpage = requests.get(product_link, headers=headers)
        new_soup = BeautifulSoup(new_webpage.content, "html.parser")
        
        # Extract product details
        name = new_soup.find("span", attrs={"id": 'productTitle'})
        price = new_soup.find("span", attrs={"class": 'a-price'})
        rating = new_soup.find("span", attrs={"class": 'a-icon-alt'})
        
        # Append data to lists if found
        if name:
            names.append(name.text.strip())
        else:
            names.append('Not Found')
        
        if price:
            prices.append(price.text.strip())
        else:
            prices.append('Not Found')
        
        if rating:
            ratings.append(rating.text)
        else:
            ratings.append('Not Found')
    
    return names, prices, ratings

# Amazon URL for PlayStation 5 search results
url = "https://www.amazon.com/s?k=playstation+5&i=specialty-aps&srs=12653393011&crid=2OQM7CA056XEG&sprefix=pla%2Cspecialty-aps%2C343&ref=nb_sb_ss_pltr-sample-20_1_3"

# Headers for the request
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'Accept-Language': 'en-US, en;q=0.5'
}

# Scrape product details
names, prices, ratings = scrape_product_details(url, HEADERS)

# Create a DataFrame to store the data
data = {
    'Name': names,
    'Price': prices,
    'Rating': ratings
}

df = pd.DataFrame(data)

# Write to CSV
df.to_csv('amazon_products.csv', index=False)

print("Scraping and writing to CSV completed.")

