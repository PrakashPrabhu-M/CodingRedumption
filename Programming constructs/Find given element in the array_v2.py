#returning the middle index
# TODO: Implement this method
def findElement(n, arr, x):
    cnt=0
    index=[]
    for i in range(len(arr)):
        if arr[i] == x:
            cnt+=1
            index.append(i)
    return index[len(index)//2+1]



def main():
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    x = int(input().strip())

    xIndex = findElement(n, arr, x)
    print(xIndex)

if __name__=="__main__":
    main()
