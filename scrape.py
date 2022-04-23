from click import option
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import urllib


IMG_QTY = 5

def start_scraping(url,queries):
    """ open webdriver """
    options = Options()
    # options.add_argument('--headless')
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options)
    driver.get(url)
    for query in queries: 
        scrape_by_query(driver,query+'\n')
    driver.close()

def create_directory(query):
    pass

def download_image(element, path):
    pass

def scrape_by_query(driver,query):
    """" start scraping query """
    print('scrapping image data for:\t{}'.format(query))
    try: 
        element = driver.find_element(By.XPATH,
                            '//*[@id="REsRA"]')
        element.clear()
        element.send_keys(query)
    except:
        # Triggered only at first page 
        driver.find_element(By.XPATH,
                            '//*[@id="sbtc"]/div/div[2]/input'
                            ).send_keys(query)

    for i in range(1, IMG_QTY):
        imgSrc = driver.find_element(By.XPATH,
                                '//*[@id="islrg"]/div[1]/div[{}]/a[1]/div[1]/img'.format(i)
                                ).get_attribute('src')
        urllib.urlretrieve(imgSrc, 'i.png')

        
    time.sleep(5)


