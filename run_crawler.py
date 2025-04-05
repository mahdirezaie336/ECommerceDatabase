from crawler import AmazonCrawler



def main():
    """
    Main function to run the crawler.
    """
    # Initialize the crawler
    crawler = AmazonCrawler()

    # Run the crawler
    crawler.run()


if __name__ == "__main__":
    main()
