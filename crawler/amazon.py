import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from .crawler import Crawler
from models import Product

import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger('AmazonCrawler')


class AmazonCrawler(Crawler):

    def __init__(self, url=None):
        self.chrome_options = Options()
        self.chrome_options.add_argument("--headless")
        self.chrome_options.add_argument("--no-sandbox")
        self.chrome_options.add_argument("--disable-dev-shm-usage")
        self.chrome_options.add_argument("--disable-gpu")
        self.chrome_options.add_argument("--window-size=1920,1080")
        self.chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                                          "(KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3")

        if not url:
            self.url = "https://www.amazon.com/s?k=men%E2%80%99s+clothing"
        else:
            self.url = url

        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=self.chrome_options)

        logger.info(f"Initialized AmazonCrawler with URL: {self.url}")

    def run(self):

        # Navigate to the Amazon search results
        logger.info(f"Navigating to {self.url}")
        self.driver.get(self.url)

        logger.info("Waiting for the page to load...")
        time.sleep(5)  # Let the page load

        # Find all products
        products_elements = self.driver.find_elements(By.CSS_SELECTOR, 'div[data-component-type="s-search-result"]')

        products = []
        for product_element in products_elements:
            try:
                # Title
                title_elem = product_element.find_element(By.TAG_NAME, 'h2')
                title = title_elem.text.strip()

                # Link to product
                link = product_element.find_element(By.CSS_SELECTOR, 'a.a-link-normal').get_attribute('href')

                # Image
                img_elem = product_element.find_element(By.CSS_SELECTOR, 'img.s-image')
                img_url = img_elem.get_attribute('src')

                # Price (can be in multiple formats — try both)
                try:
                    price_whole = product_element.find_element(By.CSS_SELECTOR, 'span.a-price-whole').text
                    price_fraction = product_element.find_element(By.CSS_SELECTOR, 'span.a-price-fraction').text
                    price = f"{price_whole}.{price_fraction}"
                except:
                    price = "N/A"

                # The discounted price
                try:
                    discounted_price = product_element.find_element(By.CSS_SELECTOR, 'span.a-text-price').text
                    discounted_price = discounted_price.replace("$", "")
                except:
                    discounted_price = "N/A"

                products.append(Product(
                    name=title,
                    original_price=price,
                    discounted_price=discounted_price,
                    purchase_url=link,
                    image_url=img_url,
                    store="Amazon",
                    category="Clothing",
                ))

            except Exception as e:
                # Skip if anything fails for this product
                pass

        logger.info(f"Found {len(products)} products.")
        self.save_products(products)

