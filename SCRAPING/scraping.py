import requests
from bs4 import BeautifulSoup
import re
import time
import pandas as pd
import numpy as np

def get_soup(BASE_PATH):
    page = requests.get(BASE_PATH)
    soup = BeautifulSoup(page.text, 'html.parser')
    return soup

BASE = 'https://www.ooyyo.com/united+states'

url = 'https://www.ooyyo.com/united+states/used-audi-q7-for-sale/c=CDA31D7114D3854F111BF66FBA75355BE1A01D6617F286/'

#This function takes next page url iteratively.
def get_page_urls(url, till):
    page_numb = 0
    url_list = []
    while page_numb < till:
        soupy = get_soup(url)
        for i in soupy.find_all('a', href = True, attrs = {'class' : "btn btn-lg btn-block btn-warning"}):
            nexty = i['href']
            url = BASE + nexty
            page_numb += 1
            url_list.append(url)
            print(url)
            time.sleep(0.8)

    return url_list

all_page_urls = get_page_urls(url, 5)

print("***********************************")

# This function takes all single car page urls in every main pages.
def get_car_urls(all_page_urls):
    x = 0
    cars = []
    for page in all_page_urls:
        page_soup = get_soup(page)
        for car in page_soup.find_all('a', href = True, attrs={'class': 'car-card-1'}):
            cars.append('https://www.ooyyo.com' + car['href'])
            time.sleep(0.8)
            x += 1
            print(f"{x}th car is added!!")
            print('https://www.ooyyo.com' + car['href'])
    return cars

all_car_urls = get_car_urls(all_page_urls)

##########################################################################
## I won't share full parts of the code, because I dont know if someone ##
##### could use this data for commercial aim or not. You should take #####
########## permission for this from administrators of website ############
##########################################################################

## At the end :
## data.to_csv('./DATA/scraped_data.csv')