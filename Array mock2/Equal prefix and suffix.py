def elementInPSS(arr,n):
    l=0
    r=len(arr)-1
    while l<=r:
        mid=l+((r-l)//2)
        if arr[mid]==n:
            return True
        if n<arr[mid]:
            r=mid-1
        else:
            l=mid+1
    return False

def elementInPPS(arr,n):
    l=0
    r=len(arr)-1
    while l<=r:
        mid=l+((r-l)//2)
        if arr[mid]==n:
            return True
        if n<arr[mid]:
            r=mid-1
        else:
            l=mid+1
    return False

def equalPrefixSuffix(n, arr):
    pps=[arr[0]]*(n-1)
    pss=[arr[n-1]]*(n-1)
    i=1
    while i<n-1:
        pps[i]=arr[i]+pps[i-1]
        i+=1
    i=n-2
    maxi=-1
    if elementInPPS(pps,arr[n-1]):
        maxi=arr[n-1]
    while i>0:
        pss[i-1]=arr[i]+pss[i]
        if elementInPSS(pps,pss[i-1]):
            maxi=max(maxi,pss[i-1])
        # if pss[i-1] in pps:
        #     maxi=max(maxi,pss[i-1])
        i-=1
    # print('pps',pps,'\npss',pss)
    return maxi

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    result = equalPrefixSuffix(n, arr)
    print(result)

if __name__=="__main__":
    main()


'''
def elementIn(arr,n):
    l=0
    r=len(arr)-1
    while l<=r:
        mid=l+((r-l)//2)
        if arr[mid]==n:
            return True
        if n<arr[mid]:
            r=mid-1
        else:
            l=mid+1
    return False

def equalPrefixSuffix(n, arr):
    pps=[arr[0]]*(n-1)
    pss=[arr[n-1]]*(n-1)
    i=1
    while i<n-1:
        pps[i]=arr[i]+pps[i-1]
        i+=1
    i=n-2
    maxi=-1
    pps=sorted(pps)
    if elementIn(pps,arr[n-1]):
        maxi=arr[n-1]
    while i>0:
        pss[i-1]=arr[i]+pss[i]
        if elementIn(pps,pss[i-1]):
            maxi=max(maxi,pss[i-1])
        # if pss[i-1] in pps:
        #     maxi=max(maxi,pss[i-1])
        i-=1
    # print('pps',pps,'\npss',pss)
    return maxi

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    result = equalPrefixSuffix(n, arr)
    print(result)

if __name__=="__main__":
    main()

'''