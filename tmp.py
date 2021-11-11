# 2 3 -> [4, 6]
first, last = map(int, input().split())
# first = 0
# last = 15
# lst = list(range(first, last))
a = [2 * n for n in range(first, last + 1)]
print(a)
