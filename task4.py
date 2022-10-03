# 4.* Задайте список из произвольных вещественных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# in
# 5
# out
# [5.16, 8.62, 6.57, 7.92, 9.22]
# Min: 0.16, Max: 0.92. Difference: 0.76

# in
# 3
# out
# [9.26, 8.5, 1.14]
# Min: 0.14, Max: 0.5. Difference: 0.36

from random import uniform

def create_random_list(count):
    ls = []
    if count <= 0:
        print ("Введено некорректное значение, повторите попытку")
        return [0.0]
    for i in range(count):
        ls.append(round(uniform(0, count), 2))
    return(ls)

def dif_min_max(ls1):
    min = ls1[0] % 1
    max = ls1[0] % 1

    for j in range(1, len(ls1)):
        num = round(ls1[j] % 1, 2)
        if num < min:
            min = num
        elif num > max:
            max = num

    dif = round(max - min, 2)
    print(f"Min: {min}, Max: {max}, Difference: {dif}")
    return dif
    
list_real = create_random_list(int(input("Введите количество элементов: ")))
print(list_real)
result = dif_min_max(list_real)
print (result)