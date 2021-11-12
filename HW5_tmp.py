import math
import random

first = 0
last = 21

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

# print('\n7. из списка целых чисел вывести количество чётных чисел, которые делятся на 5 без остатка')
# for lst in range(first, last):
#     if lst % 2 == 0 and lst % 5 == 0:
#         count25_lst = sum(lst)
#         print(count25_lst)

print('\n11. ')
five_stars = []
num_lists = 5
for i in range(num_lists):
    stars = random.sample(range(first, last), 5)
    five_stars.append(stars)
print(five_stars)

print('\n12. ')
sum_stars = list(map(sum, five_stars))
print(sum_stars)

print('\n13. ')


# def comprasion_stars(sum_stars):
#     n = len(sum_stars)
#     new_five_stars = []
#     for i in range(n):
#         if sum_stars[i] < 100:
#             stars.append(sum_stars)
#     return new_five_stars
#     print(sum_stars)
#
#
# comprasion_stars(sum_stars)
# print(sum_stars)
