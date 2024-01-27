#Операции сравнения
#boolean - bool - True, False
# print(10 == 10)
# print(30 == 50)

# print(5 != 5)
# print(100 != 100.1)

# print(100 > 500)
# print(333 > 222)

# print(600 < 599)
# print(0.1 < 0.1)

# print(1000 <= 1000)
# print(100 <= 400)

# print(10 >= 10.0)
# print(9.9 >= 9.99)

#Условие if, else, elif
# num1 = 10
# num2 = 20
# if num1 > num2:
#     print("Переменная num1 больше num2")
# else:
#     print("Переменная num2 больше num1")

# number = 13
# if number % 2 == 0:
#     print(number, "четный")
# else:
#     print(number, "нечетный")

# login = input("Логин: ")
# password = input("Пароль: ")
# if login == "geeks":
#     if password == "geeksstudents":
#         print("Вход разрешен")
#     else:
#         print("Неправильный пароль для входа")
# else:
#     print("Неправильный логин для входа")

##########################################
    
# login = input("Введите логин: ")
# password = input("Введите пароль: ")
# if login == "geeks" and password == "geeksstudents":
#     print("Вход разрешен")
# else:
#     print("Неправильный логин и пароль")

###########Google##############
    
# google_login = input("Введите почту: ")
# if google_login == "geeks@gmail.com":
#     google_password = input("Введите пароль: ")
#     if google_password == "geeksstudents":
#         print("Вход разрешен")
#     else:
#         print("Неверный пароль")
# else:
#     print("Почта не найден")

#Калькулятор
number1 = int(input("Введите первое число: "))
operator = input("+, -, *, /: ")
number2 = int(input("Введите второе число: "))
if operator == "+":
    print(number1 + number2)
elif operator == "-":
    print(number1 - number2)
elif operator == "*":
    print(number1 * number2)
elif operator == "/":
    print(number1 / number2)
else:
    print("Такого оператора нету")