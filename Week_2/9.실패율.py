N=5
stages=[2, 1, 2, 6, 2, 4, 3, 3]	
result=[3,4,2,1,5]

# n단계 실패율 구하기 = n/range(len(stages))
#result= 실패율 높은 n단계부터 낮은 n단계까지 나열 (내림차순)
stages.sort() #오름차순
print(stages) #[1, 2, 2, 2, 3, 3, 4, 6]
# 1단계는 1/8 2단계는 3/7 3단계는 2/4 4단계는 1/2 5단계는 0/1
A=0
for i in range(len(stages)):
    # print(range(len(stages))) #총길이 8
    if  7 >= i >= 0:
        A +=stages.count(i+1)
        # print(A)
        print(stages.count(i+1)/(len(stages)))
    # elif 7 >= i >= 1:
        # A +=stages.count(i+1)
        # print(len(stages)-A)
        # print(stages.count(i+1)/(len(stages)-A))   
    elif A == 8:
        break
        # A +=stages.count(i+1)
        # print(stages.count(i+1)/(len(stages)-A))
    # elif A == 8:
    #     break

