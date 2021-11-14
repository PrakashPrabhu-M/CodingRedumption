stack = []
minStack = []

def push(x):
    stack.append(x)
    if len(minStack)==0:
        minStack.append(x)
    else:
        num=minStack.pop()
        minStack.append(num)
        if num<=x:
            minStack.append(num)
        else:
            minStack.append(x)
def pop():
    if len(stack)>0:
        stack.pop()
        minStack.pop()
def findMin():
    if len(minStack)>0:
        mini=minStack.pop()
    else:
        mini=-1
    return mini

queries = int(input())

for query in range(queries):
    _type = input().strip().split()
    x = 0
    if len(_type) == 2:
        _type, x = map(int, _type)
    else:
        _type = int(_type[0])
    if _type == 1:
        push(x)
    elif _type == 2:
        pop()
    else:
        minElement = findMin()
        print(minElement)
