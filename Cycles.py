a = int(input("Введення першого числа: "))
b = int(input("Введення другого числа: "))
if a>b:
 for i in range(b,a+1):          
   if i%2 == 1:
     print(i)
   else:
     pass

if a<b:
 for i in range(a,b+1):          
   if i%2 == 1:
    print(i)
   else:
     pass
