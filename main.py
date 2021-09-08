import requests
from bs4 import BeautifulSoup
import cloudscraper
import random
import string
import os
from urllib.request import urlopen

scraper = cloudscraper.create_scraper()

print('Started!')
save_folder = 'media'

try:
    os.stat(save_folder)
except:
    os.mkdir(save_folder)

def get_link():
    letters = string.ascii_letters

    let_1 = random.choice(letters).lower()
    let_2 = random.choice(letters).lower()
    num = random.randint(1000, 9999)
    return f'https://prnt.sc/{let_1}{let_2}{num}'
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
        