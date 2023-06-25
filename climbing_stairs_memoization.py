class Solution:
    def result(self,n,t):
        if t[n]!=-1:
            return t[n]
        if n==0 or n==1:
            return 1
        t[n] = self.result(n-1,t)+self.result(n-2,t)
        #print(t,n)
        return t[n]
    def climbStairs(self, n: int) -> int:
        t = [-1 for i in range(n+1)]
        return self.result(n,t)
