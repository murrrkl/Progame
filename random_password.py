from random import randint

min_length = 3 # Минимальная возмодная длина пароля
max_length = 5 # Максимальная возможная длина пароля

length = randint(min_length, max_length) # Длина пароля

password = ""   # Пароль

for i in range(0, length, 1):
    n = randint(48, 122) # Генерирую номер символ
    random_char = chr(n) # Случайный символ
    password = password + random_char

print(password)
