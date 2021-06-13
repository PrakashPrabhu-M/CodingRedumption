def numberOfPrimesInARange(l, r):
    def prime(n):
        if n==1: return False
        for i in range(2,n//2+1):
            if n%i==0:
                return False
        return True
    return len(list(filter(prime,range(l,r+1))))


def main():
    rangeInput = input().split(' ')
    l = int(rangeInput[0])
    r = int(rangeInput[1])
    ans = numberOfPrimesInARange(l, r)
    print(ans)


if __name__ == "__main__":
    main()
