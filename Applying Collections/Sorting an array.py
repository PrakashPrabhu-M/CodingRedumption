def sortArray(n, arr):
    return sorted(arr)

def main():
    n = int(input())
    arr = input().strip().split(' ')

    sortedArr  = sortArray(n, arr)
    print(*sortedArr)

if __name__=="__main__":
    main()
