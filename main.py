from bs4 import BeautifulSoup
import cloudscraper
import os
from func import get_link, save_image

scraper = cloudscraper.create_scraper()
#no_image_template = cv2.imread('non_existent_img.jpg', cv2.IMREAD_UNCHANGED)

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
        if 'imgur' not in url:
            save_image(save_folder, url, data)
            print(os.path.join(save_folder, os.path.basename(url)))
        else:
            print("Imgur link, most likely a removed image, skipping")
    except:
        print("Image is invalid or removed, skipping")
