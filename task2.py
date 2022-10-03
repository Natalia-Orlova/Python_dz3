# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# in
# 4
# out
# [2, 5, 8, 10]
# [20, 40]

# in
# 5
# out
# [2, 2, 4, 8, 8]
# [16, 16, 4]

from random import sample

def create_random_list(count):
    if count <= 0:
        return "Введено некорректное значение, повторите попытку"
    ls = sample(range(count*2), count)
    return(ls)

def multiply_pairs(number):
    ls1 = []
    k = len(number)
    for i in range(k//2):
        ls1.append(number[i] * number[k-1-i])  
    if k % 2 == 1:
        ls1.append(number[k//2])
    return(ls1)
        
numbers = create_random_list(int(input("Введите количество элементов: ")))
print(numbers)
res = multiply_pairs(numbers)
print(res)