num = input("Please enter a number: ")
while num != 'end':
    if float(num) > int(float(num)):
        decimals = num.split('.')[1]
    else:
        decimals = 0
    print(f'decimals: {decimals}')
    num = input("Please enter a number: ")
