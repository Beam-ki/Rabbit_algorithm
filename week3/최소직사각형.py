a= ([60, 50], [30, 70], [60, 30], [80, 40])
max_x=[]
max_y=[]
        
    
for i in range(len(a)):
    b=a[i].sort()
    print(b)
    max_x.append(a[i][0])
    max_y.append(a[i][1])
    print(max(max_x)*max(max_y))