def modularExponentiation(num, power):
    return (num**power)%(10**9+7)


def main():
    num, power = map(int, input().split(' '))
    ans = modularExponentiation(num, power)
    print(ans)


if __name__ == "__main__":
    main()
