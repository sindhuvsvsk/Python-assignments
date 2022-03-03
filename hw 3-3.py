import re


def word_count(data):
    d = {}
    for w in data.split():
        d[w] = d.get(w, 0) + 1
    return d


def specific_word_count(w, length):
    new_dict = {}
    for k, c in w.items():
        if len(k) == length:
            new_dict[k] = c
    return new_dict


with open('sonnet.txt', 'r+') as f:
    content = f.read()
    content = content.lower()
    new_content = re.sub('[^a-z\n\'\-\(\)\s]', ' ', content)
    words = word_count(new_content)
    new = {}
    for i in range(2, 11):
        new[i] = specific_word_count(words, i)
        print('top 15, length of word: ', i)
        sorted_list = sorted([(value, key) for (key, value) in new[i].items()], reverse=True)[:15]
        for j in sorted_list:
            print(j[1], ":", j[0])
