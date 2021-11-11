import math

first = 0
last = 11

print('1. создать список целых чисел')
lst = list(range(first, last))
print(lst)

print('\n2. создать список целых чётных чисел')
lst = [i for i in range(first, last) if i % 2 == 0]
print(lst)

print('\n3. создать список целых нечётных чисел')
lst = [i for i in range(first, last) if i % 2 != 0]
print(lst)

print('\n4. из списка вывести только чётные числа')
for lst in range(first, last):
    if lst % 2 == 0:
        print(lst)

print('\n5. вывести из списка вывести только нечётные числа')
for lst in range(first, last):
    if lst % 2 != 0:
        print(lst)

print('\n6. вывести из списка целых чисел чётные числа которые делятся на 5 без остатка')
for lst in range(first, last):
    if lst % 5 == 0:
        print(lst)

print('\n7. из списка целых чисел вывести количество чётных чисел, которые делятся на 5 без остатка')
# for lst in range(first, last):
    # if lst % 2 ==0:
    #     print(math.fsum(lst))
# a = sum(2: 4)
# print(a)
