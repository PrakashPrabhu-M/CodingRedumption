# TODO: Implement this method
def findElement(n, arr, x):
    try:
        return arr.index(x)
    except:
        return -1

def main():
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    x = int(input().strip())

    xIndex = findElement(n, arr, x)
    print(xIndex)

if __name__=="__main__":
    main()
