def mergeIntervals(nums):
    print(nums)
    nums=sorted(nums,key= lambda a:a[0])
    l=0
    merge=[]
    while l<len(nums)-1:
        if nums[l][1]>=nums[l+1][0]:
            nums[l]=([nums[l][0],max(nums[l+1][1],nums[l][1])])
            nums.pop(l+1)
            l-=1
        l+=1
    return nums
    

if __name__ == '__main__':
    n = int(input())
    nums = []
    for i in range(n):
        row = input().split()
        row = [int(i) for i in row]
        nums.append(row)
    result = mergeIntervals(nums)
    for interval in result:
        print(*interval)
