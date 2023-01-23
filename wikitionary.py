import requests
import random
import time
import json
from lxml import html
from bs4 import BeautifulSoup
from tqdm import tqdm
import logging

# create a logging file
logging.basicConfig(filename='logging.txt', level=logging.ERROR)

# Start with the initial URL
base_url = 'https://wikitionary254.com/category/business//page/'

# Open the file containing the headers
with open('headers.json') as f:
    headers = json.load(f)
    headers_random = random.choice(headers)

for i in tqdm(range(1, 7)):
    url = base_url + str(i) + '/'
    # Make a request to the URL
    attempt = 0
    while attempt < 5:
        try:
            response = requests.get(url, headers=headers_random)
            break
        except requests.exceptions.RequestException as e:
            attempt += 1
            logging.error("Network Error: ", e)
            sleep_time = random.randint(1, 10)
            time.sleep(sleep_time)
    else:
        logging.error("Failed to connect after 5 attempts")
        continue
    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'lxml')
    # Find all the links on the page
    links = soup.find_all('div', {'class': 'inside-article'})
    for link in links:
        for el in link.find_all('header', {'class' : 'entry-header'}):

            for el_02 in el.find_all('h2', {'class' : 'entry-title'}):

                for l in el_02.find_all('a', href=True):
                    a_tags = l['href']

                    with open('url_04.txt', 'a') as f:
                        f.write(a_tags + '\n')

    time.sleep(random.randint(1,7))