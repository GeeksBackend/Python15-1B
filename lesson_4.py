#str, float, integer, bool, list, tuple
#List - списки
# name1 = "Islam"
# name2 = "Nurbolot"
# name3 = "Aktan"
# name4 = "Aziza"
# print(name1, name2, name3, name4)

# names = ["Islam", "Nurbolot", "Aktan", "Aziza"]
# print(names)

# numbers = [10, 20, 30, 40, 50]
# print(numbers)

# lst = [25, 1.5, "Geeks", True]
# print(lst)

#Индексы списков
# it_company = ["Google", "Meta", "Amazon", "Codex", "Tesla"]
# print(it_company)
# print(it_company[0])
# print(it_company[-1])
# print(it_company[1][0])

# #Срезы списков
# print(it_company[1:4:2]) #начало, конец, шаг
# print(it_company[::-1]) #перевернуть список

# #Изменения списков
# it_company.append("Neobis")
# print(it_company)

# it_company.remove("Amazon")
# print(it_company)

# it_company[2] = "Codex KG"
# print(it_company)

# it_company.append("Geeks")
# print(it_company)

# it_company.insert(0, "Test")
# print(it_company)

# it_company.pop(0)
# print(it_company)

#Tuple - кортежи
# cars = ("BMW", "Lexus", "Toyota", "Honda")
# print(cars)
# print(type(cars))
# print(cars.count("BMW"))
# print(cars.index("Lexus"))

# list_cars = list(cars)
# print(list_cars)
# list_cars.append("Zeekr")
# print(list_cars)

# cars = tuple(list_cars)
# print(cars)

import random 

# random_number = random.randint(1, 3)
# # print(random_number)
# user_number = int(input("Введите цифру от 1 до 3: "))
# if random_number == user_number:
#     print("Поздравляем вы выиграли!")
# else:
#     print("К сожелению вы проиграли случайная цифра:", random_number)

students = ["Nurbolot", "Islam", "Azatbek", "Syimyk", "Bayastan"]
print(random.choice(students))