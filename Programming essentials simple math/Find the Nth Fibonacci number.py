def nthFibonacciNumber(n):
    if n<=0:
        return 0
    if n==1:
        return 1
    return nthFibonacciNumber(n-1)+nthFibonacciNumber(n-2)

def main():
    n = int(input())
    result = nthFibonacciNumber(n)
    print(result)

if __name__=="__main__":
    main()
