import queue
s=input().split()
que=queue.Queue()
# res=0
# op1=0
# op2=0
l=list(s[0])
for i in s[1:]:
    if i not in '+-*/':
        que.put(i)

# print(que.get())
# print(que.get())
# print(que.get())
# print(que.get())
    # else:
    #     print(i)
    #     op2=int(que.get())
    #     op1=int(que.get())
    #     print(op1,op2)
    #     if i=='+':res=op1+op2
    #     elif i=='-':res=op1-op2
    #     elif i=='*':res=op1*op2
    #     elif i=='/':res=op1/op2
    #     que.put(res)
    else:
        l.append(i)
        l.append(que.get())
print(l)
print(eval(''.join([str(x) for x in l])))