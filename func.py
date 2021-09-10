import string
import random
import os
import cv2


def get_link():
    letters = string.ascii_letters

    let_1 = random.choice(letters).lower()
    let_2 = random.choice(letters).lower()
    num = random.randint(1000, 9999)
    return f'https://prnt.sc/{let_1}{let_2}{num}'

def save_image(save_folder, url, img):
    with open(os.path.join(save_folder, os.path.basename(url)), 'wb') as f:
        f.write(img.content)


#Unused for now, filtering no image found by imgur links
def match_with_template(template, img):
    try:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
    except:
        pass

    result = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    return max_val