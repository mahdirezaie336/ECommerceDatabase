from abc import ABC, abstractmethod


class Crawler(ABC):
    """
    Abstract base class for all crawlers.
    """

    @abstractmethod
    def run(self):
        """
        Run the crawler.
        """
        pass
