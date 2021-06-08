def seriesSumI(n):
    res=0
    i=1;j=3
    while n!=0:
        res+=i*j
        i+=2
        j+=2
        n-=1    
    return res


def main():
    n = int(input())

    ans = seriesSumI(n)

    print(ans)


if __name__ == "__main__":
    main()
