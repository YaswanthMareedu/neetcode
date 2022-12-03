import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check(piles,h,a):
            count = 0
            for i in range(len(piles)):
                count+= math.ceil(float(piles[i])/a)
            if count <= h:
                return True
            return False
        c=0
        if len(piles)==1:
            return math.ceil(float(piles[0])/h)
        start=0
        end = max(piles)
        while start<=end:
            mid = (start+end)//2
            if check(piles,h,mid) == True:
                end = mid-1
            else:
                start = mid+1
            
        return start