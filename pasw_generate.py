import random

letters = "zxcvbnmasdfghjklqwertyuiopZXCVBNMASDFGHJKLQWERTYUIOP1234567890!#$%*"
letters_up = "ZXCVBNMASDFGHJKLQWERTYUIOP"
numbers = "1234567890"
symbols = "!№;%*"

all_symbols = letters + letters_up + numbers + symbols

pasw = int(input("Введите длину пароля:"))

password = " "
for i in range(pasw):
    password = password + random.choice(all_symbols)

print("Ваш пароль:", password)
