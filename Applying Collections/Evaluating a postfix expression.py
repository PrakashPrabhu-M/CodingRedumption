s=input().split()
stack=[]
res=0
op1=0
op2=0
for i in s:
    if i not in '+-*/':
        stack.append(i)
        print(stack)
    else:
        print('before',stack)
        op1=stack.pop()
        op2=stack.pop()
        print(op1,op2,i)
        res=eval(f'{op2}{i}{op1}')
        stack.append(res)
        print('after',stack)
print(stack)