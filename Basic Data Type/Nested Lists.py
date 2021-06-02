#https://www.hackerrank.com/challenges/nested-list/problem

""" Given the names and grades for each student in a class of N students, 
store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, order their names alphabetically 
and print each name on a new line. 

Sample Input 0

5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39
Sample Output 0

Berry
Harry

"""
""" 
students=int(input())
marklist=[]
for i in range(students):
    name=input()
    mark=float(input())
    marklist.append([name,mark])
#print(sorted(marklist,key=lambda x:x[1]))
marks=[]
for i in marklist:
    marks.append(i[1])
second=set(marks)
second=sorted(second)[1]

seconsStudent=[]
for i in marklist:
    if i[1]==second:
        seconsStudent.append(i[0])

#print(sorted(seconsStudent))
for i in sorted(seconsStudent):
    print(i) """

marksheet = []
marksheet=[[input(),float(input())] for _ in range(int(input()))]

second_highest = sorted(list(set([marks for name, marks in marksheet])))[1]
print('\n'.join([a for a,b in sorted(marksheet) if b == second_highest]))

print([marks for name, marks in marksheet])