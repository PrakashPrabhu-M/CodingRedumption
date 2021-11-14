arrPow={}
def power(x,y):
    if y==1: return x
    if (x,y) in arrPow.keys():
        return arrPow[(x,y)]
    else:
        a=power(x,y//2)
        arrPow[(x,y//2)]=a
    if y&1:
        return x*a*a
    return a*a

def nthRoot(x, n):
    if x==0: return 0
    l=1
    r=x
    while l<=r:
        mid=(l+(r-l)//2)
        if (mid,n) in arrPow.keys():
            nthPower=arrPow[(mid,n)]
        else:
            nthPower=power(mid,n)
            arrPow[(mid,n)]=nthPower
        if nthPower==x: return mid
        elif nthPower>x:
            r=mid-1
        else:
            l=mid+1
    return r

def main():
    test = int(input())
    output = ""
    for t in range(test):
        x, n = list(map(int, input().split()))
        result = nthRoot(x, n)
        output += str(result) + "\n"
    print(output)
    # print(arrPow)

if __name__=="__main__":
    main()
