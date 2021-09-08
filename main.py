import requests
from bs4 import BeautifulSoup
import cloudscraper
import random
import string
import os
from func import get_link

scraper = cloudscraper.create_scraper()

print('Started!')
save_folder = 'media'

try:
    os.stat(save_folder)
except:
    os.mkdir(save_folder)

while True:
    url = get_link()
    print(f'URL Generated: {url}')
    soup = BeautifulSoup(scraper.get(url).content, 'html.parser')
    img = soup.find('img', id='screenshot-image')
    url = img.get('src')
    print(f'Image url: {url}')
    try:
        data = scraper.get(url)
        with open(os.path.join(save_folder, os.path.basename(url)), 'wb') as f:
            f.write(data.content)
            print("Image saved! Moving on...")
    except:
        print("Image is invalid or removed, skipping")
        