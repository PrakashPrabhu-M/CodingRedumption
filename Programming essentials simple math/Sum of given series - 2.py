def seriesSumII(A, R):
    return '{0:.5f}'.format(A/(1-R))


def main():

    [A, R] = list(map(float, input().split()))

    result = seriesSumII(A, R)

    print(result)


if __name__ == "__main__":
    main()
