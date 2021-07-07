def spiralMatrixII(n):
    top=0
    bottom=n-1
    left=0
    right=n-1
    direction=0
    #0- left to right
    #1 - top to bottom
    #2 - right to left
    #3 - bottom to top
    l=[[0 for i in range(n)] for j in range(n)]
    element=1

    while top<=bottom and left<=right:
        if direction==0:
            for i in range(left,right+1):
                #print(f'{top}{i}={element}, {direction}')
                l[top][i]=element
                element+=1
            top+=1
        elif direction==1:
            for i in range(top,bottom+1):
                #print(f'{i}{right}={element}, {direction}')
                l[i][right]=element
                element+=1
            right-=1
        elif direction==2:
            for i in range(right,left-1,-1):
                #print(f'{bottom}{i}={element}, {direction}')
                l[bottom][i]=element
                element+=1
            bottom-=1
        elif direction==3:
            #print('here')
            #print(bottom,top-1)
            for i in range(bottom,top-1,-1):
                #print(f'{left}{i}={element}, {direction}')
                l[i][left]=element
                element+=1
            left+=1
        direction=(direction+1)%4
    return l

def main():
    n = int(input())
    matrix = spiralMatrixII(n)
    for row in matrix:
        print(*row)

if __name__=="__main__":
    main()
