import requests
from bs4 import BeautifulSoup
import cloudscraper
import random
import string
import os
from func import get_link
import cv2
import numpy


scraper = cloudscraper.create_scraper()
no_image = cv2.imread('non_existent_img.jpg', cv2.IMREAD_UNCHANGED)
#cv2.imshow('Test', no_image)
#cv2.waitKey()
#v2.destroyAllWindows()

print('Started!')
save_folder = 'media'

try:
    os.stat(save_folder)
except:
    os.mkdir(save_folder)

#while True:
url = get_link()
print(f'URL Generated: {url}')
soup = BeautifulSoup(scraper.get(url).content, 'html.parser')
img = soup.find('img', id='screenshot-image')
url = img.get('src')
print(f'Image url: {url}')
try:
    data = scraper.get(url)
    #data_match = cv2.imread(data.content, cv2.IMREAD_UNCHANGED)
    #cv2.imshow('Data', data_match)
    #cv2.waitKey()
    #cv2.destroyAllWindows()
    #result = cv2.matchTemplate(data_match, no_image, cv2.TM_CCOEFF_NORMED)
    #cv2.imshow('Result', result)
    #cv2.waitKey()
    #cv2.destroyAllWindows()
    with open(os.path.join(save_folder, os.path.basename(url)), 'wb') as f:
        f.write(data.content)
        print("Image saved! Moving on...")
    data_match = cv2.imread(os.path.join(save_folder, os.path.basename(url)), cv2.IMREAD_UNCHANGED)
    cv2.imshow('Data', data_match)
    cv2.waitKey()
    cv2.destroyAllWindows()
    data_match = cv2.cvtColor(data_match, cv2.COLOR_BGR2GRAY)
    no_image = cv2.cvtColor(no_image, cv2.COLOR_BGR2GRAY)
    result = cv2.matchTemplate(data_match, no_image, cv2.TM_CCOEFF_NORMED)
    cv2.imshow('Result', result)
    cv2.waitKey()
    cv2.destroyAllWindows()
except:
    print("Image is invalid or removed, skipping")
