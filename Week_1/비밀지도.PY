n=5
arr1=[9, 20, 28, 18, 11]
arr2=[30, 1, 21, 17, 28]
# 출력=["#####","# # #", "### #", "# ##", "#####"]
# arr1,2의 10진수들을 2진수로 변경뒤
# arr2의 와비교해서 둘중하나라도 1이라면 1로변환 후 return


for i in arr1[0,n+1]:
    save = []
    
    while True:
        a = int(num / 2)
        b = int(num % 2)
        save.insert(0, b)       
        if a != 0:
            num = a
        else:
            break
    final = ''.join(map(str, save))
    print(final)

