import re

# Solution1
print('Solution1:')
s = "An email was sent from student@sjsu.edu to inquiries@gmail.com"
domains = re.findall('@(\w+)\.', s)
print(domains)

# Solution2
# Example1
print('Solution2:')
s = "An email was sent from a student@sjsu.edu to inquiries@gmail.com"
vowel_words = re.findall(r"\b[aeiouAEIOU]\w*", s)
print(vowel_words)

# Example2
fruits = "apple orange pear grapes pineapple avocado strawberry"
fruits_vowel_words = re.findall(r'\b[aeiouAEIOU]\w*', fruits)
print(fruits_vowel_words)

# Solution3
# Example1
print('Solution3:')
s = "An email was sent from student@sjsu.edu to inquiries@gmail.com"
words = re.findall(r'\b[a-zA-Z]{5,7}\b', s)
print(words)

# Example2
w = "apple orange pear grapes pineapple avocado strawberry"
words1 = re.findall(r'\b[a-zA-Z]{5,7}\b', w)
print(words1)

# Solution4
print('Solution4:')
s1 = "123-456-7890 and 1234567890 and (123) 456-7890"
# y = re.findall(r'\d{3}[-.]\d{3}[-.]\d{4}|\d{10}', s1)
# print(y)
y = re.findall(r'\d{3}-\d{3}-\d{4}|\d{10}|\(\d{3}\) \d{3}-\d{4}', s1)
print(list(y))
