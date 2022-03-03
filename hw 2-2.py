score = input("Enter score: ")
if score.isalpha():
    print('Bad Score')
    exit()
a = float(score)
if 0.9 <= a < 1.0:
    print("A")
elif 0.8 <= a < 0.9:
    print("B")
elif 0.7 <= a < 0.8:
    print("C")
elif 0.6 <= a < 0.7:
    print("D")
elif 0 < a < 0.6:
    print("F")
else:
    print('Bad Score')
#(46 <= ord(char) <= 57):
