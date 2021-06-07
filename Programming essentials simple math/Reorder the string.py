def stringPermutation(n, s, per):
    lis=[None]*n
    per=[i-1 for i in per]
    for n,i in enumerate(per):
        lis[i]=s[n]
    return ''.join(lis)

def main():
    n = int(input())
    s = input()
    per = list(map(int, input().strip().split(' ')))

    result = stringPermutation(n, s, per)
    print(result)

if __name__=="__main__":
    main()
