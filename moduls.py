#В Python импортировать модули можно несколькими способами
#1 - импортировать сам модуль
# import lesson_8 #без окончания .py

# print(lesson_8.hello_world())
# print(lesson_8.add(10, 20))
# print(lesson_8.it_courses('Python'))
# print(lesson_8.it)

#2 - импортировать отдельные определения из модуля
# from lesson_8 import hello_world, it 

# print(hello_world())
# print(it)

#3 - импортировать всё содержимое модуля сразу
# from lesson_8 import *

# print(hello_world())
# print(it)
# print(it_courses("Java"))
# print(add(100, 400))

# from test import numbers, names
# from lesson_8 import chet_nechet, welcome_name

# chet_nechet(numbers)
# welcome_name(names)