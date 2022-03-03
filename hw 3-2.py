try:
    fname = input("Enter filename:")
    with open(fname, 'r') as f:
        print(f.read())
        f.seek(0)
        grades_list = []
        total = 0
        for row in f:
            flag = 0
            values = row.split(',')[1]
            studentid = row.split(',')[0]
            if not studentid.isdigit():
                raise ValueError
            values = values.strip()
            grades_list.append(values)
            for char in values:
                if 46 <= ord(char) <= 57:
                    flag = 1
                else:
                    flag = 0
                    raise ValueError
            if flag == 1:
                s = float(values)
                total = total + s
    count = str(len(grades_list))
    average = total / len(grades_list)
    avg = str(average)
    high = str(max(grades_list))
    low = str(min(grades_list))
    with open('results.txt', 'w+', newline='') as f1:
        f1.writelines('No of students in file:' + count + '\n' + 'Average of grades:' + avg + '\n' +
                      'Highest grade:' + high + '\n' + 'Lowest grade:' + low)
except FileNotFoundError:
    print("Oops, the file you entered is incorrect!!! ")
except IndexError:
    print("Empty grades file")
except ZeroDivisionError:
    print("Length of the grades in the denominator is zero")
except ValueError:
    print("studentid or grades must be numeric")
