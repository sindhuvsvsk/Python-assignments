import re
from queue import LifoQueue


class HTMLVerifier:

    def __init__(self, file):
        self.file = file

    def read_file(self):
        with open(self.file, 'r') as f:
            return f.read()

    def verify_tags(self, data):
        tokens = re.split('(<[^>]*>)', data)[1::2]
        s = LifoQueue()
        unbalanced = []
        for word in tokens:
            if '/' not in word:
                s.put(word)
            else:
                while not s.empty():
                    if word.replace('/', '') == s.queue[-1]:
                        s.get()
                        break
                    else:
                        unbalanced.append(s.get())
        return unbalanced

    def unbalanced_tags(self, unbal_tags):
        if len(unbal_tags) == 0:
            print("Tags are balanced")
        else:
            print("Unbalanced tags:")
            print(unbal_tags[::-1])


text = HTMLVerifier("html.txt")  # Here the filename I used on my local is html.txt
content = text.read_file()
tags = text.verify_tags(content)
text.unbalanced_tags(tags)
