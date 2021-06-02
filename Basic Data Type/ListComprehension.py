#x,y,z,n=[int(input()) for _ in range(4)]
x,y,z,n=eval(",".join(['int(input())']*4))

l=[[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k!=n]
print(l)