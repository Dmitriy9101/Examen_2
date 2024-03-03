# def sum_numbers(n): #Функция ( def )
#     summa = 0
#     for i in range(1, n+1):
#         summa += i
#     return summa

# a = sum_numbers(500)
# print (a)

# def sum_str(*a): #Для сколько угодных аргументов
#     res = ''
#     for i in a:
#         res += i
#     return res
# print(sum_str('-','e','a'))


# -------------------------------------------
# Импорт функции из другого файла


# import modul

# modul.max1(5,9)

# print(modul.max1(5, 9))


# -----------

# from modul import max1 # Импортировать конкретную функцию

# print(max1(20,21))
# --------------------
# from modul import * # Импортировать все функции из файла

# print(max1(20,21))
# -------------------
# import modul as m # переименовал нужный модуль в 'm'

# print (m.max1(1,2))
# ------------------------------

# def fib(n):
#     if n in [1,2]:
#         return 1
#     return fib(n-1) + fib(n-2)


# list_1 = []
# for i in range(1,10):
#     list_1.append(fib(i))
# print(list_1)

# -------------------------------

# def quick_sort(array):
#     if len(array) <= 1:
#         return array
#     else:
#         pivot = array[0]
#     less = [i for i in array[1:] if i <= pivot]
#     greated = [i for i in array[1:] if i > pivot]
#     return(quick_sort(less) + [pivot] + quick_sort(greated))

# print(quick_sort([10,5,2]))

# ------------------------------------
# Сортировка слиянием

# def merge_sort(nums):
#     if len(nums) > 1:
#         mid = len(nums) // 2
#         left = nums[:mid]
#         right = nums[mid:]
#         merge_sort(left)
#         merge_sort(right)
#         i = j = k = 0
#         while i < len(left) and j < len(right):
#             if left[i] < right[j]:
#                 nums[k] = left[i]
#                 i += 1
#             else:
#                 nums[k] = right[j]
#                 j += 1
#             k += 1

#         while i < len(left):
#             nums[k] = left[i]
#             i =+ 1
#             k =+ 1

#         while j < len(right):
#             nums[k] = right[j]
#             j =+ 1
#             k =+ 1

# list1 = [1,2,4,5,23,54,23,54,23,99]
# merge_sort(list1)
# print(list1)