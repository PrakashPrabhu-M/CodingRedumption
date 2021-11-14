def equalPartition(n, arr):
    i=0
    j=n-1
    left=arr[0]
    right=arr[j]
    while i<j:
        # print(left,right)
        if left>right:
            j-=1
            right+=arr[j]
        elif right>left:
            i+=1
            left+=arr[i]
        elif j-i==2:
            return i+1
        else:
            i+=1
            j-=1
    return -1 

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    result = equalPartition(n, arr)
    print(result)

if __name__=="__main__":
    main()
