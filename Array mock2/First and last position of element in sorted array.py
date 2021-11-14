def first(nums,target):
        l=0
        r=len(nums)-1
        first=-1
        while l<=r:
            mid=l+(r-l)//2
            if nums[mid]==target:
                first=mid
                r=mid-1
            elif nums[mid]>target:
                r=mid-1
            else:
                l=mid+1
        return first

def last(nums,target):
    l=0
    r=len(nums)-1
    last=-1
    while l<=r:
        mid=l+(r-l)//2
        if nums[mid]==target:
            last=mid
            l=mid+1
        elif nums[mid]>target:
            r=mid-1
        else:
            l=mid+1
    return last

def findFirstAndLastPositionOfElementInSortedArray(nums, target):
    ans = [-1, -1]
    ans[0]=first(nums,target)
    ans[1]=last(nums,target)
    return ans

a=findFirstAndLastPositionOfElementInSortedArray(list(map(int,input().split())),int(input()))
print(a)