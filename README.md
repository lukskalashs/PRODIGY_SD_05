# Amazon Product Scraper

This Python script scrapes product details (name, price, rating) from Amazon search results for PlayStation 5 and saves the data to a CSV file.

## Requirements

- Python 3.x
- Required Python libraries: `beautifulsoup4`, `requests`, `pandas`

## Installation

1. Clone the repository or download the script.
2. Install dependencies:

## Usage

1. Modify the `url` variable in the script to change the Amazon search results page if needed.
2. Run the script:
3. The script will output `amazon_products.csv` containing scraped data.

## Script Explanation

The script uses BeautifulSoup and requests libraries to scrape product details from Amazon. It defines a function `scrape_product_details` to extract names, prices, and ratings of products from individual product pages linked from the search results. The scraped data is then stored in a Pandas DataFrame and saved to a CSV file.

---

Feel free to adjust the sections or add more details as per your specific needs or audience. This readme provides a brief overview of what the script does, how to install dependencies, and how to run it.

