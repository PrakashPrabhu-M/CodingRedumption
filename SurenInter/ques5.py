n=int(input())
s=input().split()
s2='X'*s.count('X')+'Y'*s.count('Y')+'Z'*s.count('Z')
for i in s2:
    print(i,end=' ')