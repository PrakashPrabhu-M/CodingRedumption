def oddNumbers(n):
    for i in range(1,n+1,2):
        yield(i)

def main():
    n = int(input())

    ans = oddNumbers(n)
    print(*ans)


if __name__ == "__main__":
    main()
