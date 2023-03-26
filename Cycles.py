a = int(input("Enter a number a: "))
b = int(input("Enter a number b: "))
if a>b:
 for i in range(b,a+1):          
   if i%2 == 1:
     print(i, end = "\t")
   else:
     pass

if a<b:
 for i in range(a,b+1):          
   if i%2 == 1:
    print(i, end = "\t")
   else:
     pass
