n=5
arr1=[9, 20, 28, 18, 11]
arr2=[30, 1, 21, 17, 28]
# 출력=["#####","# # #", "### #", "# ##", "#####"]
# arr1,2의 10진수들을 2진수로 변경뒤
# arr2의 와비교해서 둘중하나라도 1이라면 1로변환 후 return


# for i in arr1[0,n+1]:
#     save = []
    
#     while True:
#         a = int(num / 2)
#         b = int(num % 2)
#         save.insert(0, b)       
#         if a != 0:
#             num = a
#         else:
#             break
#     final = ''.join(map(str, save))
#     print(final)
# for i in arr1:
#     a=bin(i)[2:].zfill(5)
# for j in arr2:
#     b=bin(j)[2:].zfill(5)
#     a=a.replace('2','1')
#     b=b.replace('2','1')
#     c=int(a)+int(b)
#     print(c)
    
# def solution(n, arr1, arr2):
answer=[''] * n
for i in range(len(arr1)):
    bin1 = bin(arr1[i])[2:].zfill(n)
    bin2 = bin(arr2[i])[2:].zfill(n)
    for j in range(n):
        if bin1[j] == '0' and bin2[j] == '0':
            answer[i]+=' '
        else:
            answer[i]+='#'
        print(answer)
    # return answer

n=5
arr1=[9, 20, 28, 18, 11]
arr2=[30, 1, 21, 17, 28]
A=bin(100)
# [2:]

print(A)