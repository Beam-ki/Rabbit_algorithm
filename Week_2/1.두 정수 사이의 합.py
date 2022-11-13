a=5
b=3
c=0
if a<b:
    for i in range(a,b+1):
        c +=i
        print(c)        
elif a>b:
    for i in range(b,a+1):
        c +=i
        print(c)
elif a==b:
    print(a)
