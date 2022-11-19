import re
import random
import string

length = int(input("Enter the length of the password you want to generate: "))
password = ""

letters = "абвгдеёжзийклмнопрстуфхцчшщьыъэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЫЪЭЮЯ"
characters_of_password = string.ascii_letters + string.digits + string.punctuation + letters  # creating a pool of characters

correct_password_check = re.compile('^.*(?=[A-ЯA-Z]{2,})(?=[а-яa-z]){2,}(?!.*\\s)(?!.*\\d{3})(?=.+[а-яА-Я]).*$')  # regex to check randomly generated passwords

checked = False

while not checked:
    password = ''.join(random.choice(characters_of_password) for char in range(length))

    if not correct_password_check.match(password):
        checked = False

    else:
        checked = True

print(f'Your randomly generated password is: {password}')
