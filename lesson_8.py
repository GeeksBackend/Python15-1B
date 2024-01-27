#Модули Python
def hello_world():
    return "Hello World"

def add(num1:int=1, num2:int=1) -> int:
    return num1 + num2 

def it_courses(language:str) -> str:
    return f"Programming Language {language}"

it = "Geeks"

def chet_nechet(numbers:[tuple, list]) -> str:
    for num in numbers:
        if num % 2 == 0:
            print(num, "четный")
        else:
            print(num, "нечетный")

def welcome_name(names:list) -> str:
    for name in names:
        print("Здраствуйте", name)

#Работа с файлами Python
# f = open('hello.txt', 'w')
# f.write("Hello World And Geeks")
# f.close()

# r = open('hello.txt', 'r')
# print(r.read())
# r.close()

# python_file = open('file_test.py', 'w')
# python_file.write('print("Hello World")')
# python_file.close()

# read_python_file = open('lesson_8.py', 'r')
# print(read_python_file.read())
# read_python_file.close()
        
# test = open('file_test.py', 'w')
# test.write('print("Hello Geeks")')
# test.close()

# encode = open('test.txt', 'w', encoding='utf-8')
# encode.write("Привет всем и привет Geeks!")
# encode.close()

# read_enconde = open('test.txt', 'r', encoding='utf-8')
# print(read_enconde.read())
# read_enconde.close()

# with open('close.txt', 'w', encoding='utf-8') as close:
#     close.write("С помощью with можно не закрывать файл, он сам закроется")