def findTrailingZeros(n):
    cnt=0
    while n//5:
        cnt+=n//5
        n//=5
    return cnt
n = int(input())
result = findTrailingZeros(n)
print(result)
