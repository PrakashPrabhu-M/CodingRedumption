def pascalsTriangle(n):
    l=[[0 for i in range(n)] for j in range(n)]
    l[0][0]=1
    for i in range(1,n):
        for j in range(n):
            l[i][j]=l[i-1][j]+l[i-1][j-1]
    #res=[x[:i] for x in l for i in ]
    res=[]
    for line,n in zip(l,range(n)):
        res.append(line[:n+1])
    return res

if __name__ == '__main__':
    n = int(input())
    result = pascalsTriangle(n)
    for row in result:
        print(*row)