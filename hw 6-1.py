import re
from collections import Counter

words = re.findall(r'\w+', open('sonnet.txt').read().lower())
#print(words)
c = Counter(words)
print(c)
result = Counter()
length, n = input("Enter length of word and # terms to return: ").split(' ')
print('top ' + n, 'length of word: ' + length)
n = int(n)
for key, value in c.items():
    if len(key) == int(length):
        result[key] = value
for item in list(result.most_common(n)):
    print(item[0], ":", item[1])
