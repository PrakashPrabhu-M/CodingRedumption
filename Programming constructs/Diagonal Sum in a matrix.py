# TODO: Implement this method
def diagonalSum(matrix, n):
    sumOfDiagonal=0
    for i,j in zip(range(n),range(n)):
        sumOfDiagonal+=matrix[i][j]
    return sumOfDiagonal


def main():
    n = int(input())

    matrix = []

    for i in range(0, n):
        row = list(map(int, input().strip().split(' ')))
        matrix.append(row)
    
    ans = diagonalSum(matrix, n)
    print(ans)


if __name__ == "__main__":
    main()
