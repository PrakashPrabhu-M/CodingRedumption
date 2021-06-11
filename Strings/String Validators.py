#https://www.hackerrank.com/challenges/string-validators/problem
""" Sample Input

qA2
Sample Output

True
True
True
True
True """
""" 
In the first line, print True if  has any alphanumeric characters. Otherwise, print False.
In the second line, print True if  has any alphabetical characters. Otherwise, print False.
In the third line, print True if  has any digits. Otherwise, print False.
In the fourth line, print True if  has any lowercase characters. Otherwise, print False.
In the fifth line, print True if  has any uppercase characters. Otherwise, print False. """

s=input()
print(any(map(lambda x:x.isalnum(),[a for a in s])))
print(any(map(lambda x:x.isalpha(),[a for a in s])))
print(any(map(lambda x:x.isdigit(),[a for a in s])))
print(any(map(lambda x:x.islower(),[a for a in s])))
print(any(map(lambda x:x.isupper(),[a for a in s])))
