# Алгоритм 1

# 1. Напишите алгоритм сортировки выбором (selection sort)
# Рассмотрите, как алгоритм работает в отладчике (debug)
# список для сортировки 
# lst = [3, 14, 1, 7, 9, 8, 11, 6, 4, 2]
1) Алгоритм сортировки выбором:

1. Инициализировать переменную i равной 0.
2. До тех пор, пока i меньше длины списка:
    - Найти минимальный элемент в списке с индексами от i до конца списка.
    - Если найденный минимальный элемент не равен текущему элементу с индексом i:
        - Поменять местами найденный минимальный элемент и текущий элемент с индексом i.
    - Увеличить i на 1.

Пример реализации на Python:

def selection_sort(lst):
    for i in range(len(lst)):
        min_index = i
        for j in range(i, len(lst)):
            if lst[j] < lst[min_index]:
                min_index = j
        if min_index != i:
            lst[i], lst[min_index] = lst[min_index], lst[i]

# Проверка работы сортировки выбором на списке lst
lst = [3, 14, 1, 7, 9, 8, 11, 6, 4, 2]
selection_sort(lst)
print(lst)

# Дополнительно
# 2. Создайте функцию min/max, которая использует алгоритм сортировки написанный выше

2) Функция min/max, использующая алгоритм сортировки выбором:
Для нахождения минимального и максимального элемента списка можно использовать аналогичный алгоритм сортировки выбором, но с некоторыми изменениями. Например, для нахождения минимального элемента можно искать его только в первой половине списка (с индексами от 0 до длины списка // 2), а для нахождения максимального элемента - только во второй половине списка (с индексами от длины списка // 2 до конца списка).

# Пример реализации функции min/max на основе алгоритма сортировки выбором:
 def min_max(lst):
    min_val = lst[0]
    max_val = lst[-1]
    for i in range(len(lst) // 2):
        if lst[i] < min_val:
            min_val = lst[i]
        if lst[-i-1] > max_val:
            max_val = lst[-i-1]
    return min_val, max_val

# Проверка работы функции min_max на списке lst
lst = [3, 14, 1, 7, 9, 8, 11, 6, 4, 2]
min_val, max_val = min_max(lst)
print("Минимальный элемент:", min_val)
print("Максимальный элемент:", max_val)
