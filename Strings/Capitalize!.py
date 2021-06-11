#https://www.hackerrank.com/challenges/capitalize/problem
""" Sample Input

chris alan
Sample Output

Chris Alan """

s=input().split()
for i in s:
    print(i.capitalize(),end=' ')