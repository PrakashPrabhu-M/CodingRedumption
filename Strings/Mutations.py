#https://www.hackerrank.com/challenges/python-mutations/problem
""" Sample Input

STDIN           Function
-----           --------
abracadabra     s = 'abracadabra'
5 k             position = 5, character = 'k'
Sample Output

abrackdabra """

word=input()
pos,char=input().split()
pos=int(pos)

final=word[:pos]+char+word[pos+1:]
print(final)

""" Or you can also use list """