def countDistinctElements(n, b, arr):
    if n<b: return []
    res=[None]*(n-b+1)
    left=0
    right=b
    d={a:arr[left:right].count(a) for a in arr[left:right]}
    right+=1
    while right<n:
        res[left]=len(d.keys())
        if d[arr[left]]==1:
            d.pop(arr[left])
        else:
            d[arr[left]]-=1

        if arr[right] in d.keys():
            d[arr[right]]+=1
        else:
            d[arr[right]]=1
        left+=1
        right+=1

    return res

def main():
    n, b = list(map(int, input().strip().split(' ')))
    arr = list(map(int, input().strip().split(' ')))

    result = countDistinctElements(n, b, arr)
    print(*result)

if __name__=="__main__":
    main()
