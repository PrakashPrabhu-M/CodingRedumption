from math import gcd
n=int(input())
def lucky(x):
    if not(1<=x<=n):
        return False
    if n%x==0:
        return False
    if gcd(n,x)==1:
        return False
    return True
    
for i in range(n):
    if lucky(i):
        print(i)