#https://www.hackerrank.com/challenges/designer-door-mat/problem
""" Sample Input

9 27
Sample Output

------------.|.------------
---------.|..|..|.---------
------.|..|..|..|..|.------
---.|..|..|..|..|..|..|.---
----------WELCOME----------
---.|..|..|..|..|..|..|.---
------.|..|..|..|..|.------
---------.|..|..|.---------
------------.|.------------ """

row,colum=map(int,input().split())
row//=2
char='.|.'
string='WELCOME'
cnt=1
for i in range(row):
    print((char*cnt).center(colum,'-'))
    cnt+=2
print(string.center(colum,'-'))
cnt-=2
for i in range(row):
    print((char*cnt).center(colum,'-'))
    cnt-=2