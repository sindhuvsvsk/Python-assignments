l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

a = [i + 5 for i in l]
print(f'a. {a}')

b = [i for i in l if i % 2 == 1]
print(f'b. {b}')

c = [3 ** i for i in l if i % 2 == 0]
print(f'c. {c}')

d = [2 * i if i % 2 == 0 else 3 * i for i in l]
print(f'd. {d}')

e = [i + 5 for i in l if 2 < i <= 8]
print(f'e. {e}')
