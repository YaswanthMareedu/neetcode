class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        for i in range(len(nums)):
            if (target-nums[i]) in d:
                return [i,nums.index(target-nums[i])]
            else:
                d[nums[i]]=1