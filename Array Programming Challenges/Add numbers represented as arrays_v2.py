def addNumbers(n, m, firstNum, secondNum):
    res=[]
    c=0
    for i,j in zip(range(n-1,-1,-1),range(m-1,-1,-1)):
        res.insert(0,(firstNum[i]+secondNum[j]+c)%10)
        c=(firstNum[i]+secondNum[j]+c)//10
        #print(f'{firstNum[i]}+{secondNum[j]}+{c}',(firstNum[i]+secondNum[j]+c),res,c)
    l=abs(m-n)
    add=firstNum[:l] if n>m else secondNum[:l]

    for i in range(l-1,-1,-1):
        res.insert(0,(add[i]+c)%10)
        c=(add[i]+c)//10
        #print(f'{add[i]}+{c}',(firstNum[i]+secondNum[j]+c),res,c)
    if c!=0:
        res.insert(0,c)
    return res

def main():
    n, m = map(int, input().split())
    firstNum = list(map(int, input().split()))
    secondNum = list(map(int, input().split()))
    result = addNumbers(n, m, firstNum, secondNum)
    print(*result, sep="")


if __name__ == "__main__":
    main()
