from venv import create
from click import option
from regex import R
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import urllib
import shutil
import os


DATA_DIR = 'dataset_v2_less_label'
IMG_QTY = 500

def start_scraping(url,queries):
    """ open webdriver """
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options)
    driver.get(url)
    for query in queries: 
        scrape_by_query(driver,query+'\n')
    driver.close()

def create_directory(query):
    parentDir = os.getcwd()
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)   
    dataDir = os.path.join(parentDir,DATA_DIR)
    queryDir = os.path.join(dataDir,query[:-1])
    print(queryDir)
    
    if not os.path.exists(queryDir):
        os.makedirs(queryDir)
    else:
        shutil.rmtree(queryDir,ignore_errors=True)           
        os.makedirs(queryDir)

    print('Directory {} created'.format(query[:-1]))
    
    return queryDir

def scrape_by_query(driver,query):
    """" start scraping query """
    queryDir = create_directory(query)
    print('Scrapping image data for:  {}'.format(query))
    # click 'sign in' pop up
    try:
        driver.find_element(By.XPATH,
                            '//*[@id="yDmH0d"]/c-wiz/div/div/c-wiz/div/div/div/div[2]/div[2]/button'
                            ).click()
    except:
        pass
    
    # input fields to searchbar
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

    # scrape and download image
    errorImage = 0
    for i in range(1, IMG_QTY+1):
        try:
            imgElement = driver.find_element(By.XPATH,
                                    '//*[@id="islrg"]/div[1]/div[{}]/a[1]/div[1]/img'.format(i)
                                    )
            imgSrc = imgElement.get_attribute('src')
            urllib.request.urlretrieve(imgSrc, os.path.join(queryDir,'{}.png'.format(i)))
        except:
            print("Failed getting {}".format(i))
            errorImage += 1

        if i%20 == 1 and i!=1 :
            webdriver.ActionChains(driver).scroll(0,0,0,10000, origin=imgElement).perform()
            time.sleep(5)
    
    # print summary        
    print('Non-Error Image : {}'.format(IMG_QTY-errorImage))
    time.sleep(5)


