def zeroOnes(n, arr):
    l=0
    r=n-1
    while l<r:
        mid=(r+l)//2
        if arr[mid]==1:
            while arr[mid-1]==1 and mid>0:
                mid-=1
            return mid
        l=mid+1
    if arr[l]==1:
        return l
    return -1
        

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    result = zeroOnes(n, arr)
    print(result)

if __name__=="__main__":
    main()
