n=int(input())
s=int(input(),2)
cnt=0
temp=0
for i in range(n):
    s=s<<1
    print(s,s&1)
    if s&1==0:
        cnt+=1
print(cnt)
