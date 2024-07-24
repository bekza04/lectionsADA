"=======================функции===================="
# функции это именнованый блок кода который может принимать аргументы и возвращать результат 

# def my_sum(x, y):
#     return x +y

# res = my_sum(5, 6)
# print(res)




#DRY - do not repeat yourself, функции соблюдают этот принцип


"======================аргументы и параметры========================="
# параметры это переменные внутри функции значения котрые мы задаем при определении функции 
# аргументы это переменные которые мы передаем при вызове функций

# def my_len(obj): #obj - параметр 
#     count = 0
#     for element in obj:
#         count += 1
#     return count
# res = my_len([]) # аргумент 


"====================== виды парметров ============================"
# 1 обязательные
# 2 необязательные
# 2.1 с дефолтным значением 
# 2.2  *args (все позиционные аргументы которые не попали в обязательные и с дефолтным значегием
# 2.3 **kwargs (все лишние именнованные аргументы)
"================виды аргументов================="
# 1 позиционные (по позиции)
# 2 именованные (по названиб (параметр= значение))

# def add_or_add_10(num1, num2 = 10):
#     """
#     складвает два числа
#     если второе число не предать сложть первое с 10
#     """
#     return num1 + num2
# number = 5
# print(add_or_add_10())
# print()

"========================== * =================================="
# list1 = list(range(1, 11))
# list2 = [*range(1, 11)]
# print(list1)         
# print(list2)

# dict1 = {"a": 1, "b": 2, "c": 3}
# dict2 = {**dict1}
# list1 = [*dict1]
# print(dict1)
# print(dict2)
# print(list1)


# def func(a, b=10, *args, **kwargs):
#     print("a -", a)
#     print("b -", b)
#     print("args -", args)
#     print("kwargs -", kwargs)

# func(1, 2, 3, 4, 5, 6,)
# a - 1
# b - 10
# args - ()
# kwargs - {}


"===============lambda================"
#lambda анонимная функция котоая записывается в одеу строку 


"=====================calculator=============="

# calc = {
#     "+": lambda n1, n2: n1 + n2,
#     "-": lambda n1, n2: n1 - n2,
#     "*": lambda n1, n2: n1 * n2,
#     "/": lambda n1, n2: n1 / n2,
#     "/": lambda n1, n2: n1 // n2,
#     "%": lambda n1, n2: n1 % n2,
# }

# def main():
#     try:
#         num1 = int(input("put number: "))
#         num2 = int(input("put number: "))
#         oper = input("choose operation")
#         func =calc[oper]
#         res = func(num1, num2)
#         print(num1, oper, num2, "=", res)

#     except ValueError:
#         print("put number")
#     except KeyError:
#         print("mistaken operation")
#     except ZeroDivisionError:
#         print("not possible")

# while True:
#     main()
#     if input("finish (yes/no)?").lower() =="yes":
#         break

db = [
    {"name": "Bekzaada", "password": hash("bekz04")},
    {"name": "Bekzaada2", "password": hash("bekz05")}
]

def in_database(name):
    for user in db:
        if user["name"] == name:
            return True
    return False


def register(name, password1, password2):
    if in_database(name):
        raise Exception("такой пользователь уже существует")
    if password1 != password2:
        raise Exception("пароли не совпадают")
    user = {"name": name, "password":hash(password1)}
    db.append(user)

    return "вы успешно зарегестрировались"

def login(name, password):
    if not in_database(name):
       raise Exception("пользователь не найден")
    for user in db:
        if user["name"] == name:
            if user["password"] != hash(password):
                raise Exception("пароль не верный")
            
    return "Вы успешно вошли в систему"


    










