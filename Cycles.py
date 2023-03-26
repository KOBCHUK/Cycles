a = int(input('Enter num a: '))
b = int(input('Enter num b: '))
for i in range(a, b+1):
    print(i)
for i in range(b, a-1, -1):
 print(i)
for i in range(a, b+1):
    if i%7 == 0:
        print(i)
counter = 0
for i in range(a, b+1):
    if i%5 == 0:
        counter += 1
        print(counter)
