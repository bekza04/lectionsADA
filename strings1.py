'===========строки=========='
#строки это неизмяемые типы данных, котроый предназначен для хранеия текста, заключенного в одинарные или двойные кавчки

str_ = 'строка с одинарыми кавычками'
str2 = "строка с двойными кавычками"

str3 = """
многострочный текст в дваойных кавычках, модно исаользовать любые кавычки
"""
str4 = "Don\t"
str5 = "Don't"

"============Конкатенация============"

name = "Bekzaada"
last_name = "sarkunbek"
full_name = name + " " + last_name
print(full_name) #Bekzaada sarkunbek

print("hello" * 10) #hellohellohellohellohellohellohellohellohellohello

"===========экранизация строк============="
#"\n" - переносит на новую строку
print("hello\nworld")  
#hello
#world

# \t - табуляция
print("hello\tworld") #hello   world

# '\'' отображение
# " \"" отображение

# \v - перенос на новую строку со смещением вправо на длину предыдущей строки 
print("hello\vworld\vmy\vname")
#hello
     #world
          #my
            #name

# r\ - перенос каретки на начало строки 
print("hello\rhi") #hillo

"===========форматирование строк================"
title = "iphone 15"
price = 1000
print(f"название: {title}\nцена: {price}")
#название: iphone 15
#цена: 1000

"===========Методы строк==================="
# методы - это функции, которые относятся к определенному классу типу данных, к ним мы обращаемся через точку

print(dir(str)) #показывает все методы определенного типа данных

string = "hello"
print(string.upper()) #HELLO

string = "HELLO"
print(string.lower()) #hello

print("HellO".swapcase ()) #hELLo

print("hello world".title()) #Hello World
print("hello world".capitalize()) #Hello world


print("hello".center(11, "-")) #---hello---

print("world".count("w")) #1

print("hello".startswith("h")) #true. Проверяет начинается ли строка с заданного символа и возвращает либо true false

print("hello".endswith("o")) #true. Проверяет заканчивается ли строка с заданного символа и возвращает либо true false

print("hello world".islower()) #true
print("hello wOrld".islower()) #false

print("HELLO WORLD".isupper()) #true
print("hello world".isupper()) #false

#прверяет состоит ли строка поносьтю из чисел
print("1231231232123".isdigit()) #true
print("123123123рвыоы23".isdigit()) #false


print("njdckjd".isalpha()) #true
print("123123djbdcj123".isalpha()) #false

print("hello123".isalnum()) #true
print("1223".isalnum()) #true

print("hello world my name is Bekzaada".split()) #['hello', 'world', 'my', 'name', 'is', 'Bekzaada']
print("hello world my name is Bekzaada".split("l")) #['he', '', 'o wor', 'd my name is Bekzaada'] 


print("-".join(['hello', 'world', 'my', 'name', 'is', 'Bekzaada'])) #hello-world-my-name-is-Bekzaada

#strip - убирает пробелы слева и справа
string ='         hello           '
print(string.strip)


"===============индексы======================"
#индексы - порядковый номер в последовательности (символа в строке)(иекчация начинается с нуля)

"h e l l o"
#0 1 2 3 4
#     -2 -1

string1 = "hello world"
print(string1[0]) #h

#срез-подстройка нашей строки 
print(string1[0:5]) #hello
print(string1[0:4]) #hell

print(string1[::-1]) #dlrow olleh












