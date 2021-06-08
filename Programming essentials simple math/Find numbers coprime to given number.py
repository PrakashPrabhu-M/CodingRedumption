""" from math import lcm
#gcd=m*n/lcm(m,n)
def gcd(a, b):
    print(f'a={a}, b={b}')
    if (a == 0):
        return b
    return gcd(b % a, a)
print(gcd(5,4)) """

def coprimeNumbers(n):
    def gcd(a,b):
        if a==0:return b
        return gcd(b%a,a)
    cnt=0
    for i in range(n):
        if gcd(n,i)==1:
            cnt+=1
    return cnt

def main():
    n = int(input().strip())

    countCoPrime = coprimeNumbers(n)
    print(countCoPrime)


if __name__ == "__main__":
    main()
