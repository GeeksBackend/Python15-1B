#Функции Python
"""Функции в Python представляет собой особый участок
кода который можно вызывать обратишись к нему по имени,
которым он был назван. Функции можно создать при
помощи оператора Python - def"""

# def hello():
#     print("Hello World")
# hello() #вызов функции по имени hello

# def it_geeks():
#     print("Geeks - айти курсы в Оше")
#     print(10 + 44)
# it_geeks()

# def add():
#     num1 = int(input("Первое число: "))
#     num2 = int(input("Второе число: "))
#     print(num1 + num2)
# add()

# def mult(num1, num2): #num1, num2 - параметры
#     print(num1 + num2)
# mult(10, 40) #10, 40 - это аргументы к функции
# mult(400, 700)
# mult(1000, 3220)

# def welcome(names:list) -> str:
#     for name in names:
#         print(f"Здравствуйте {name[0]}.")
# list_names = ["Kurmanbek", "Beksultan", "Islam"]
# welcome(list_names)
# welcome()

# def chet_nechet(number:int=2) -> str:
#     "Фунция для вычисления четных и нечетных чисел"
#     if number % 2 == 0:
#         print(number, "четный")
#     else:
#         print(number, "нечетный")
# chet_nechet(100)
# chet_nechet()

# def izogramma(word:str="Geeks") -> bool:
#     # print(word)
#     if len(set(word.lower())) == len(word.lower()):
#         print(True)
#     else:
#         print(False)
# izogramma("Telegram")
# izogramma("IT")
# izogramma("BMW")
# izogramma("TelEgram")

# def it_geeks():
#     return "Geeks Osh IT"
# print(it_geeks())

# import time 
# def chet_time():
#     start_time = time.time()
#     print("Hello World")
#     # time.sleep(1)
#     print("Geeks")
#     end_time = time.time()
#     print(start_time, end_time)
#     print(end_time - start_time)
# chet_time()

import random

def generate_password():
    letters = "qwertyuiopasdfghjklzxcvbnm1234567890!@#$%^&*()"
    # random_letter = random.choice(letters)
    # print(random_letter)
    result = ""
    for i in range(10):
        random_letter = random.choice(letters)
        # print(random_letter)
        result += random_letter
        # result = result + random_letter
    print(result)
generate_password()