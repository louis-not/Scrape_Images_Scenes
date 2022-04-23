from scrape import start_scraping
import pandas as pd

def get_queries():
    url_queries = 'https://raw.githubusercontent.com/louis-not/Scrape_Images_Scenes/main/label_clean.csv?token=GHSAT0AAAAAABTUS5CQUY7WPI5LT4LFEK7MYTELM7A'

    df = pd.read_csv(url_queries, names = ['queries'])
    queries = list()
    for data in df['queries']:
        queries.append(data)
    return queries


def main():
    url = 'https://images.google.com'      
        
    queries = ['pantai','gunung','museum']    
    # queries = get_queries()
    print(queries)
    start_scraping(url,queries)
    print("DONE !!!")

    
if __name__ == '__main__':
    main()