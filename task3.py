# 3. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Без использования встроенной функции преобразования, без строк.
# in
# 88
# out
# 1011000

# in
# 11
# out
# 1011

def convert_dec_to_bin(number):
    bin_list = []
    while number > 0:
        bin_list.insert(0,number % 2)
        number = number // 2
    return bin_list

res = convert_dec_to_bin(int(input("введите число: ")))
print(*res, sep="")