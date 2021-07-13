def incrementNumber(n, number):
    res=[]
    inc=1
    c=0
    for i in range(n-1,-1,-1):
        res.insert(0,(number[i]+inc+c)%10)
        c=(number[i]+inc+c)//10
        inc=0
        #print(res,c)
    if c!=0:
        res.insert(0,c)
    return res

def main():
    n = int(input())
    number = list(map(int, input().split()))
    result = incrementNumber(n, number)
    print(*result, sep="")


if __name__ == "__main__":
    main()
