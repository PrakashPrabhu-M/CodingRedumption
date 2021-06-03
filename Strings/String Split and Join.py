#https://www.hackerrank.com/challenges/python-string-split-and-join/problem
""" Sample Input

this is a string   
Sample Output

this-is-a-string """
sentence=input().split()
print('-'.join(sentence))

""" def split_and_join(line):
    return line.replace(' ','-') """