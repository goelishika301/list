a=0
b=1
print(a,b)
n=int(input("enter a number"))
for i in range (n-2):
    c=a+b
    a=b
    b=c
    print(c)
