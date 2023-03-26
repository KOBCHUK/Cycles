a = int(input('Enter a number a: '))
b = int(input('Enter a number b: '))
for i in range(a, b+1):
    print(i, end = '\t')
for i in range(b, a-1, -1):
 print(i, end = '\t')
for i in range(a, b+1):
    if i%7 == 0:
        print(i)
counter = 0
for i in range(a, b+1):
    if i%5 == 0:
        counter += 1
print(counter)
