left=13
right=17
list=0
for a in range(left, right+1):
    result=0
    for b in range(1 ,a+1):
        if a % b ==0:
            result +=1
    if result % 2 == 0:
        list += a
    else:
        list -= a
    
print(list)