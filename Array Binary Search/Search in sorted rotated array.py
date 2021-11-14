# SearchInRotatedSortedArray solution
def findInRotatedArray(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    ans = -1
    last_elm=nums[-1]
    l=0
    r=len(nums)-1
    side=None
    if nums[0]<=target: side=1
    else: side =2
    while l<r:
        mid=(l+r)//2
        if nums[mid]==target: return mid
        if nums[l]<=nums[mid] and side==1:
            if target>nums[mid]:
                l=mid+1
            else:
                r=mid-1
        elif nums[r]>=nums[mid] and side==2:
            if target>nums[mid]:
                l=mid+1
            else:
                r=mid-1
        else:
            if nums[l]<=nums[mid] and side==2:
                l=mid+1
            else:
                r=mid-1


    if nums[l]==target:
        return l

    return ans; 

if __name__ == '__main__':
    n = int(input().strip())
    nums = [int(i) for i in input().strip().split()]
    q = int(input().strip())

    for i in range(q):
        target = int(input().strip())
        print(findInRotatedArray(nums, target))
