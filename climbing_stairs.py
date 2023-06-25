class Solution:
    def result(self,n):
        if n==0 or n==1:
            return 1
        return self.result(n-1)+self.result(n-2)
    def climbStairs(self, n: int) -> int:
        return self.result(n)
        
