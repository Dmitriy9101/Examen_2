# # Напишите программу, которая на вход принимает два числа A и B, и 
# # возводит число А в целую степень B с помощью рекурсии.

# def f(a, b): # число, степень
#     if b == 0:
#         return 1
#         # b = b + 1
#         # print(b)
#     return a * f(a, b - 1)



# # a = int(input("Какое число возводим в степень ?"))
# # b = int(input("В какую степень возводим? "))
# # print(Deegre(a, b))

# # ------------------------------------------------

# # Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух 
# # целых неотрицательных чисел. Из всех арифметических операций 
# # допускаются только +1 и -1. Также нельзя использовать циклы.

# def sum(a, b):
#     if b == 0:
#         return a
#     return 1 + sum(a, b - 1)




# a = int(input("Введите первое число " ))
# b = int(input("Введите второе число " ))
# print(sum(a, b))    