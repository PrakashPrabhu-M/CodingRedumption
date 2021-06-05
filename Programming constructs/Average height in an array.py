# TODO: Implement this method
def averageHeight(n,a):
    return round(sum(a)/n,5)

def main():
    n=int(input())
    a=list(map(float,input().split()))
    result = averageHeight(n,a)
    print(result)

if __name__=="__main__":
    main()
