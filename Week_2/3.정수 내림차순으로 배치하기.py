n=118372
list=[]
for i in map(int,str(n)):
    list.append(i)
    A=sorted(list,reverse=True)
    answer=''.join(map(str, A))
    print(int(answer))

# sorted 함수는 sorted(iterable, *, key=None, reverse=False)와 같이 정의되어 있습니다. 이 reverse가 False로 되어있기 때문에 오름차순으로 정리가 됩니다. 그러므로 쓰실 때 인자로 reverse=True를 적어주시면 원하시는 결과가 나올겁니다. 자세한건 공식문서를 참