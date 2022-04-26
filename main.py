from scrape import start_scraping
import pandas as pd

def get_queries():
    url_queries = 'new_categories_label.csv'

    df = pd.read_csv(url_queries)
    queries = list()
    for data in df['label']:
        queries.append(data)
    return queries


def main():
    url = 'https://images.google.com'      
    # queries = ['mountain','beach','museum']    
    queries = get_queries()
    print(len(queries))
    start_scraping(url,queries)
    print("DONE !!!")

    
if __name__ == '__main__':
    main()