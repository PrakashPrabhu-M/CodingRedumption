def nextLargerElement(arr):
    res=[]
    isEmpty=lambda a: len(a)==0
    def top(stack):
        if not isEmpty(stack):
            a=stack.pop()
            stack.append(a)
            return a
        return False

    stack=arr[:1]
    for i in range(1,len(arr)):
        if isEmpty(stack):
            stack.append(arr[i])
        else:
            while (top(stack)<arr[i]) and (not isEmpty(stack)):
                res.append([top(stack),arr[i]])
                stack.pop()
            else:
                stack.append(arr[i])
    print(res)
    return res


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().strip().split()))
    result = nextLargerElement(arr)
    print(*result)
