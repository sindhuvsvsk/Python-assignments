def student_list(s):
    word = input("Enter grade record (press Enter to stop): ")
    while word != '':
        x, y = word
        # x = word.split(',')[0]
        # y = word.split(',')[1]
        s.append((x, y))
        word = input("Enter grade record (press Enter to stop): ")
    return s


slist = []
records = student_list(slist)
fname = input("Enter filename to save:")
with open(fname, 'w+', newline='') as f:
    for s in records:
        f.write("%s, %s \n" % (s[0], s[1]))
with open(fname, 'r') as f:
    print(f.read())
