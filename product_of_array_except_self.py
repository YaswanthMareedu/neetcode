class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pd_fr=1
        pd_back=1
        n=len(nums)
        res=[]
        for i in nums:
            res.append(pd_fr)
            pd_fr*=i
        #print(res)
        for i in range(n):
            res[n-i-1]*=pd_back
            #print(pd_back,res)
            pd_back*=nums[n-i-1]
        #print(res)
        return res