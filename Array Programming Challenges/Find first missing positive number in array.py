def firstMissingPositive(nums):
    flag=1
    while flag:
        flag=0
        for i in range(len(nums)):
            if 0<=nums[i]<len(nums) and i!=nums[i]:
                flag=1
                temp=nums[nums[i]]
                nums[nums[i]]=nums[i]
                nums[i]=temp
    print(nums[:15])
    print(nums[15:25])
    print(nums[25:])
    #print(len(nums))
    for i in range(len(nums)):
        #print(i,(i+1), nums[i],(i+1)!=nums[i])
        if (i)!=nums[i] and i!=0:
            return i

if __name__ == '__main__':
    n = int(input())
    nums = []
    if n > 0:
        nums = input().split()
        nums = [int(i) for i in nums]

    result = firstMissingPositive(nums)
    print(result)

