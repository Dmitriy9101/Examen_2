# Задача №31. Решение в группах Последовательностью Фибоначчи 
# называется последовательность чисел a0 , a1 , ..., an , ..., 
# где a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1). 
# Требуется найти N-е число Фибоначчи Input: 7 Output: 21

# def fib(n):
#     if n in range(0,2):
#         return 1
#     return fib(n-1) + fib(n-2)


# m = int(input())
# print(fib(m))

# Задача №35. Решение в группах Напишите функцию, которая принимает 
# одно число и проверяет, является ли оно простым Напоминание: 
# Простое число - это число, которое имеет 2 делителя: 1  и n(само число) 
# Input: 5 Output: yes

# def simple(n, d = 2):
#     if d * 2 > n:
#         return True
    
#     elif n % d == 0:
#         return False
    
#     return simple(n, d + 1)

# m = int(input())
# print(simple(m))


# Задача №37. Решение в группах 15 минут Дано натуральное число N
# и последовательность из N элементов. 
# Требуется вывести эту последовательность в обратном порядке. 
# Примечание. В программе запрещается объявлять массивы и использовать 
# циклы (даже для ввода и вывода).
# Input:    2 -> 3 4 Output: 4 3
# N = 2
# def Coup(n): # Coup - Переворот
    