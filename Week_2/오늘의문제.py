num_list=[1, 2, 4, 56, 5]	
a=[0,0]
for i in num_list:
    if i % 2 == 0:
        a[0] +=1
    else:
        a[1] +=1
    print(a)
# 변수명은 for 문 밖에서 !!!!!!제발!!