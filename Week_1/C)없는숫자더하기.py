a= [1,2,3,4,6,7,8,0]	
b= [1,2,3,4,6,7,8,0,5,9]
c=[x for x in b if x not in a]
asd=list(set(b)-set(a))
print(sum(c))
