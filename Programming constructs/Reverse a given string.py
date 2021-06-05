# TODO: Implement this method
def reverseNum(num):
    cp=num
    rev=0
    while cp:
        digit=cp%10
        rev=rev*10+digit
        cp//=10
    return rev

def main():
    num = int(input())
    reversedNum = reverseNum(num)
    print(reversedNum)


if __name__ == "__main__":
    main()