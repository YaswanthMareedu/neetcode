class Solution:
    def climbStairs(self, n: int) -> int:
        t = [0 for i in range(n+1)]
        #return self.result(n,t)
        for i in range(n+1):
            if i==0 or i==1:
                t[i]=1
            if i>=2:
                t[i]=t[i-1]+t[i-2]
        #print(t)
        return t[n]
        
