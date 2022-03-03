def count(string, char):
    # Count variable
    count = 0
    for i in string:
        # Checking character in string
        if i == char:
            count += 1
    return count


string = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
length = len(string)
print(f'Given String :{string}')
print(f'Length : {length}')
r1 = count(string, 'A')
r2 = count(string, 'T')
print(f'A count:{r1}')
print(f'T count:{r2}')
percentage = (r1 + r2) / length
print(f'Percentage of A and T :{percentage:.4f}')
