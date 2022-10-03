# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).
# in
# 5
# out
# [10, 2, 3, 8, 9]
# 22

# in
# 4
# out
# [4, 2, 4, 9]
# 8
from random import sample
def create_random_list(count):
    if count <= 0:
        return "Введено некорректное значение, повторите попытку"
    ls = sample(range(count*2), count)
    return(ls)

def sum_odd_elem(ls1):
    s = 0
    for i in range(0, len(ls1), 2):
        s += ls1[i]
    return s

num = int(input("Введите количество элементов: "))
lst = create_random_list(num)
print(lst)
result = (sum_odd_elem(lst))
print(f"сумма элементов на нечетных позициях = {result}")
