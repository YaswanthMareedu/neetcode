import math
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        s = math.ceil((sum(nums)+target)/2)

        n = len(nums)
        #print(s)
        #t = [[0 for j in range(s+1)] for i in range(len(nums)+1)]
        t= {}
        coins = nums
        s = target
        #Memoization code
        def findways(coins,s,n,target):
            if n<=0:
                if s==target:
                    return 1
                else:
                    return 0
            if (s,n) in t:
                return t[(s,n)]

            t[(s,n)]=findways(coins,s-coins[n-1],n-1,target)+findways(coins,s+coins[n-1],n-1,target)
            return t[(s,n)]
        return findways(coins,0,n,target)
