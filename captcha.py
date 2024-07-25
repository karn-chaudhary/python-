
import random

def create_captcha():

    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

#generate the captch 5 character
    captcha = ''.join(random.choise(characters)for _ in range(5))

    return captcha

#testing the captcha multipal time
for _ in range(5):
    print(create_captcha())
