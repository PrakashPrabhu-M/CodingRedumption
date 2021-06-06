# TODO: Implement this method
def patternPrintingI(n):
    l=[]
    for i in range(1,n+1):
        l.append('* '*i)
    return l


def main():
    n = int(input())

    pattern = patternPrintingI(n)

    for i in pattern:
        print(i)


if __name__ == "__main__":
    main()
