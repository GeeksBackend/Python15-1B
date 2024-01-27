#Типы данных
#integer - int - 10, 20, 30, 55
#float - 10.5, 11.1, 0.111, 0.5
#string - str - "Hello", "Geeks", "World"
#boolean - bool - True, False

#Строки и методы строк
#В python есть 4 вида строк:
# str_example_one = 'Hello. I\'m backend developer'
# print(str_example_one)

# str_example_two = "Hello. I'm backend developer"
# print(str_example_two)

# str_example_three = """Hello. I'm backend developer.
# My name's Kurmanbek"""
# print(str_example_three)

# str_example_four = '''Hello. I'm backend developer.
# My name's Kurmanbek'''
# print(str_example_four)

# name = "Nurbolot"
# surname = "Erkinbaev"
# print(surname + ' ' + name) #Конкатинация - сложение строк

# name = input("Введите свое имя: ")
# print("Здраствуйте", name, "Как ваши дела?")

# number1 = input("Введите первое число: ")
# number2 = input("Введите второе число: ")
# print(int(number1) + int(number2))

#Индексы строк
# it = "Geeks"
#      #01234
# print(it)
# print(it[0])
# print(it[3])

# hello = "Hello World"
#         #012345678910
# print(hello)
# print(hello[6:11])
# print(hello[0:5])
# print(hello[::2]) #Начало, Конец, Шаг
# print(hello[::-1])
# print(hello[1::2])

name = "kurMANbeK"
print(name)
print(name.title())
print(name.upper())
print(name.lower())
print(name.index('u'))