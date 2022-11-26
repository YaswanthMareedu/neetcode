class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans=0
        s=set(nums)
        for i in nums:
            if i-1 not in s:
                c=0
                while i+c in s:
                        c+=1
            
                ans=max(c,ans)
        return ans
        