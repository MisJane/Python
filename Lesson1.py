print('хочу текст с пробелами' + ' или' + ' другими знаками' + ' в' + ' Python', sep=' 1 ')
print('хочу текст с пробелами', 'или', 'другими знаками', 'в', 'Python', sep=' ')
print('хочу текст с пробелами', 'или', 'другими знаками', 'в', 'Python')
print()

line1 = 'хочу перенос строки вот тут'
line2 = 'а потом продолжить текст'
print(line1, "\n")
print(line2, "\n")

# 1) Создать переменную типа String
s = 'стринги'
# 2) Создать переменную типа Integer
i = 3
# 3) Создать переменную типа Float
fl = 3.0705
# 4) Создать переменную типа Bytes
# 5) Создать переменную типа List
# 6) Создать переменную типа Tuple
# 7) Создать переменную типа Set
# 8. Создать переменную типа Frozen set
# 9) Создать переменную типа Dict

print(s, 'is', type(s))
print(i, 'is', type(i))
print(fl, 'is', type(fl))

print("\n" * 2)
name = input('Input your name:')
print('Hello, ', name, '!')
