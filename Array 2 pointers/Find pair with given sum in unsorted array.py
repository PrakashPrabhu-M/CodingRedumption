def twoSum(nums, target):
    i=0
    j=len(nums)-1
    l=[]
    while i<j and i<len(nums) and j<len(nums):
        #print(nums[i],nums[j])
        if nums[i]+nums[j]<target:
            i+=1
        elif nums[i]+nums[j]>target:
            j-=1
        else:
            l.append(i)
            l.append(j)
            j-=1
            i+=1
    #print(l)
    return l

if __name__ == '__main__':
    n = int(input())
    nums = input().split()
    nums = [int(i) for i in nums]
    target = int(input())
    result = twoSum(nums, target)
    print(result[0],result[1])
