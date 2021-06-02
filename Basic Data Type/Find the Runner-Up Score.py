#https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
"""
Sample Input 0

5
2 3 6 6 5
Sample Output 0

5
"""

partispants=int(input())
scores=[int(x) for x in input().split()][:partispants]
unique=set(scores)
print(sorted(unique)[-2])