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
    #print(soup)
    img = soup.find('img', id='screenshot-image')
    print('Image found!')
    url = img.get('src')
    print('Image acquired!')
    print(url)
    data = scraper.get(url)
    with open(os.path.join(save_folder, os.path.basename(url)), 'wb') as f:
        #image = open(f'{save_folder}/{url[22:-4]}.png', 'wb')
        #image.write(data.content)
        #image.close()
        f.write(data.content)
    #print('Image saved!')