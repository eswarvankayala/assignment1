a=0
b=1
k=int(input("enter the required the length of the series"))
print(a)
print(b)
for i in range(0,k+1):
    c=a+b
    print(c)
    a=b
    b=c
    
