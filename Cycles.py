a = int(input('Enter a number a: '))
b = int(input('Enter a number b: '))
for i in range(a, b+1):
    if i%7 == 0:
        print(i, end = "\t")
