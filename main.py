from scrape import start_scraping

def main():
    url = 'https://images.google.com'

    # queries = list()
    # with open('label_clean.csv', 'r', ) as f:
        
    queries = ['pantai','gunung','museum']    
    start_scraping(url,queries)
    print("DONE !!!")

    
if __name__ == '__main__':
    main()