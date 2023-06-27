class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        #Method 1 (recursive but we get time limit exceeded)
        t = [-1 for i in range(len(coins))]
        n = len(coins)
        def findways(coins,s,n):
            if s<0:
                return 0
            if s==0:
                return 1
            if n<0:
                return 0

            return findways(coins,s-coins[n],n)+findways(coins,s,n-1)
        
        #return findways(coins,amount,n-1)

        #Recursion with memoization (Solved)
        t = {}
        n = len(coins)
        s = amount
        def findways(coins,s,n):
            if s<0:
                return 0
            if s==0:
                return 1
            if n<=0:
                return 0
            if (s,n) in t:
                return t[(s,n)]

            t[(s,n)]=findways(coins,s-coins[n-1],n)+findways(coins,s,n-1)
            return t[(s,n)]
        #return findways(coins,amount,n)
