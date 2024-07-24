


from unittest import result

num1 = int(input("введи первое число"))
num2 = int(input("введи второе число"))

op = input("Выберите операцию из следующих +-*/%//**: ")

     
if op == '+':
            result = num1 + num2
elif op == '-':
            result = num1 - num2
elif op == '*':
            result = num1 * num2
elif op == '/':
            result = num1 / num2
elif op == "%":
            result = num1 % num2
elif op == "//":
            result = num1 // num2
elif op == "**":
            result = num1 ** num2
else:
 print("Данной операции нет в системе.")

print("ответ:",result)

continue_calc = input("Хотите продолжить (yes/no)?: ")

print = ("До свидания!")
