l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# solution1
a = map(lambda x: x + 5, l)
print(f'a. {list(a)}')

# solution2
b = filter(lambda x: x % 2 == 1, l)
print(f'b. {list(b)}')

# solution3
# evenlist = list(filter(lambda x: x % 2 == 0, l))
evenlist = list(range(0, 10, 2))
c = map(lambda x: 3 ** x, evenlist)
print(f'c. {list(c)}')

# solution4
d = map(lambda x: x * 2 if x % 2 == 0 else x * 3, l)
print(f'd. {list(d)}')

# solutions5
oddlist = list(filter(lambda x: x % 2 == 1, l))

# e = map(lambda x: x if (x < 4) else (2 * x if 4 < x < 10 else False), oddlist)
# print(f'e. {list(e)}')

e = map(lambda x: x if x < 4 else 2 * x, oddlist)
print(f'e. {list(e)}')

