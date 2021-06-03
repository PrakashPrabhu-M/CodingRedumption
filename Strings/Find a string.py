#https://www.hackerrank.com/challenges/find-a-string/problem
""" Sample Input

ABCDCDC
CDC
Sample Output

2
 """
string=input()
sub=input()
count=0
for i in range(len(string)):
    if sub==string[i:len(sub)+i]:
        count+=1

print(count)
""" 
string, substring = (input().strip(), input().strip())
print(sum([ 1 for i in range(len(string)-len(substring)+1) if string[i:i+len(substring)] == substring])) """