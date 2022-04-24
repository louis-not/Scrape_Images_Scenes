from scrape import start_scraping
import pandas as pd

def get_queries():
    url_queries = 'label_clean.csv'

    df = pd.read_csv(url_queries, names = ['queries'])
    queries = list()
    for data in df['queries']:
        queries.append(data)
    return queries


def main():
    url = 'https://images.google.com'      
    
    # queries = ['pantai','gunung','museum']    # FOR TRIAL
    queries = get_queries()
    print(len(queries))
    start_scraping(url,queries)
    print("DONE !!!")

    
if __name__ == '__main__':
    main()