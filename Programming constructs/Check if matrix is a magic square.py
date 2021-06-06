# TODO: Implement this method
def checkMagicSquare(n, matrix):
    sumOfRows=[sum(x) for x in matrix]
    #print(sumOfRows)
    sumOfColumns=[]
    tempSum=0
    for i in range(n):
        for j in range(n):
            tempSum+=matrix[i][j]
        sumOfColumns.append(tempSum)
        tempSum=0
    #print(sumOfColumns)
    if len(set(sumOfColumns))==1 and len(set(sumOfRows)) and set(sumOfColumns)==set(sumOfRows):
        return True
    return False

def main():
    n = int(input())
    matrix = []

    for i in range(0, n):
        row = list(map(int, input().split(' ')))
        matrix.append(row)

    isMagicSquare = checkMagicSquare(n, matrix)

    if(isMagicSquare):
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
