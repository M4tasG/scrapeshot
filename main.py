from bs4 import BeautifulSoup
import cloudscraper
import os
from func import check_csv, get_link, save_image, check_csv

scraper = cloudscraper.create_scraper()
#no_image_template = cv2.imread('non_existent_img.jpg', cv2.IMREAD_UNCHANGED)

print('Started!')
check_csv()
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
    img_url = img.get('src')
    print(f'Image url: {img_url}')  
    try:
        data = scraper.get(img_url)
        if 'imgur' not in img_url:
            print("Not an imgur link, saving image")
            save_image(save_folder, url, img_url, data)
        else:
            print("Imgur link, most likely a removed image, skipping")
    except:
        print("Image is invalid or removed, skipping")
