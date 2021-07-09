def addNumbers(n, m, firstNum, secondNum):
    a=''.join(str(x) for x in firstNum)
    b=''.join(str(x) for x in secondNum)
    return str(int(a)+int(b))

def main():
    n, m = map(int, input().split())
    firstNum = list(map(int, input().split()))
    secondNum = list(map(int, input().split()))
    result = addNumbers(n, m, firstNum, secondNum)
    print(*result, sep="")


if __name__ == "__main__":
    main()
