def mul(x,lis):
    carry=0
    print(lis,type(lis))
    res=[]
    for i in lis:
        print(i,type(i))
        temp=list(str(i*x+carry))
        carry=temp[:-1]
        res.append(temp[-1])
    if carry:
        res.append(carry)
    return res            
x=10
a=mul(x,[4,2,3])
print(a)