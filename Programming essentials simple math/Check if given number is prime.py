def checkPrime(t, nums):
    for num in nums:
        flag=0
        #print(num,end=' ')
        if num<=1:
            #print('here',num)
            yield False
            continue
        for i in range(2,num//2+1):
            if num%i==0:
                #print(num)
                yield False
                flag=1
                break
        if flag==0:
            yield True

def main():
    t = int(input())
    nums = []
    for i in range(0,t):
        n = int(input())
        nums.append(n)
    ans = checkPrime(t,nums)

    for i in ans:
        if(i == False):
            print("false")
        else:
            print("true")


if __name__=="__main__":
    main()
#