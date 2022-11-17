def binarysearch(start,end,nums,target):
    if start>end:
        return -1
    mid=(start+end)//2
    if nums[mid]<target:
        return binarysearch(mid+1,end,nums,target)
    elif nums[mid]>target:
        return binarysearch(start,mid-1,nums,target)
    else:
        return mid
        
print(binarysearch(0,5,[0,1,2,3,4,5],5))