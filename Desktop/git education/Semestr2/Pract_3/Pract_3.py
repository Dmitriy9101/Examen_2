# Задание 1.Дан список чисел. Найдите количество уникальных чисел

# list_1 = [1, 1, 2, 0, -1, 3, 4, 4]

# list_2 = []

# for i in list_1:
#     if i not in list_2: ## Если i нет в list_2
#         list_2.append(i) # append- добавить

# print(len(list_2))


# print(len(set(list_1))) !! Быстрый способ

#----------------------------------------------------------------

# Создание нового множества
# new_set = set{}

# Задача №19. Решение в группах Дана последовательность из N целых чисел и
# число K. Необходимо сдвинуть всю последовательность (сдвиг - циклический)
# на K элементов вправо,  K – положительное число. Input:
# [1, 2, 3, 4, 5] k = 3 Output:  [4, 5, 1, 2, 3] Примечание:
# Пользователь может вводить значения списка или список задан изначально.

# list_3 = [1, 2, 3, 4, 5]

# k = 1

# k = k % len(list_3) # len - количество чисел в списке

# list_output = list_3[-k:] + list_3[:-k]

# print(list_3[-k:])
# print(list_3[:-k])
# print(list_output)

# list_3 = [1, 2, 3, 4, 5]

# print((list_3).pop(2)) pop- Убрать число под индексом
# print((list_3).remove(4))
# print(list_3)

# for i in range(2):
#     temp = list_3.pop()
#     list_3.insert(0, temp)
#     print(list_3)

# Задача №21. Решение в группах Напишите программу для печати всех
# уникальных значений в словаре. Input:  [{"V": "S001"}, {"V": "S002"},
#  {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "},
#    {" VIII ":" S007 "}] Output: {'S005', 'S002', 'S007', 'S001', 'S009'} 
# Примечание: Список словарей задан изначально. Пользователь его не вводит

# dic = [{"V": "S001"}, {"V": "S002"},
#  {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "},
#    {" VIII ":" S007 "}]

# ---------------------------------------
# s = set()
# for i in dic:
#     for k, v in i.items():
#         s.add(v)

# print(s)

# ------------------------------------------

# s = set()
# for i in dic:
#      for v in i.values(): #values - Для перебора именно ЗНАЧЕНИЙ в справочнике
#         s.add(v)

# print(s)