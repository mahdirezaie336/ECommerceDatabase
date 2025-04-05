from abc import ABC, abstractmethod
from typing import List

from models import Product

import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger('AmazonCrawler')


class Crawler(ABC):
    """
    Abstract base class for all crawlers.
    """

    def save_products(self, products: List[Product]):
        """
        Save products to the database.
        """
        print("Saving products to the database...")
        print(products)
        pass

    @abstractmethod
    def run(self):
        """
        Run the crawler.
        """
        pass
