def reverseBits(n):
    i=3
    rev=0
    while i>=0:
        a=1 if n&(1<<i) else 0
        if a:
            rev=rev|1<<(4-(i+1))
        i-=1
    return rev

def main():
    T = int(input())
    for test in range(T):
        n = int(input())
        result = reverseBits(n)
        print(result)

if __name__=="__main__":
    main()
