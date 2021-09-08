import string
import random

def get_link():
    letters = string.ascii_letters

    let_1 = random.choice(letters).lower()
    let_2 = random.choice(letters).lower()
    num = random.randint(1000, 9999)
    return f'https://prnt.sc/{let_1}{let_2}{num}'