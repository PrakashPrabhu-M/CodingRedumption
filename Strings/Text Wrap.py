#https://www.hackerrank.com/challenges/text-wrap/problem
""" 
Sample Input 0

ABCDEFGHIJKLIMNOQRSTUVWXYZ
4
Sample Output 0

ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ """

s,n=input(),int(input())
for i in range(0,len(s),n):
    print(s[i:n+i])

l=[s[i:n+i] for i in range(0,len(s),n)]
print(l)

l=[i*j for i in range(1,5) for j in range(1,10)]
print(l)