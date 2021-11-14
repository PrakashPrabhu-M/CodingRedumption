day,pages=map(int,input().split())
x=-1
flag=0
while x<pages:
    x+=1
    tot=0
    for i in range(1,day+1):
        tot+=i*x+i
        if tot>=pages:
            flag=1
            print(x)
            break
    if flag:
        break

