def numberOfDivisorsAndSum(n):
    fact=[]
    for i in range(1,n+1):
        if n%i==0:
            fact.append(i)
    fact=set(fact)
    return [len(fact),sum(fact)]

def main():
    n = int(input())
    list=numberOfDivisorsAndSum(n)
    print(*list)

if __name__=="__main__":
    main()
