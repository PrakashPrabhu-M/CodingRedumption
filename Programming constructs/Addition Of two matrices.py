# TODO: Implement this method
def additionOfMatrix(n, m, matrixOne, matrixTwo):
    addMat=[]
    for row1,row2 in zip(matrixOne,matrixTwo):
        addMat.append([e1+e2 for e1,e2 in zip(row1,row2)])
    return addMat
    

def main():
    n, m = map(int, input().split(' '))

    matrixOne = []
    matrixTwo = []

    for i in range(n):
        row = list(map(int, input().split(' ')))
        matrixOne.append(row)
    
    for i in range(n):
        row = list(map(int, input().split(' ')))
        matrixTwo.append(row)
    
    sumMatrix = additionOfMatrix(n, m, matrixOne, matrixTwo)

    for i in sumMatrix:
        print(*i)

if __name__=="__main__":
    main()