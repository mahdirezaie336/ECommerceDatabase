from abc import ABC, abstractmethod
from typing import List

from models import Product
from database import get_db

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
        db = get_db()
        logger.info("Saving products to the database...")
        for product in products:
            try:
                db.add(product)
                db.commit()
                db.refresh(product)
                logger.info(f"Saved product: {product}")
            except Exception as e:
                logger.error(f"Failed to save product {product}: {e}")
                db.rollback()

    @abstractmethod
    def run(self):
        """
        Run the crawler.
        """
        pass
