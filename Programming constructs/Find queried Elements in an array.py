
# TODO: Implement this method


def findElementQuery(n, arr, q, query):
    res=[]
    for i in query:
        try:
            res.append(arr.index(i))
        except ValueError:
            res.append(-1)
    return res



def main():
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    q = int(input().strip())

    query = []

    for i in range(q):
        x = int(input().strip())
        query.append(x)

    result = findElementQuery(n, arr, q, query)

    print(*result, sep="\n")


if __name__ == "__main__":
    main()
