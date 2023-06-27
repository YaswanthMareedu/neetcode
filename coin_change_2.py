class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        t = {}
        n = len(coins)
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
        return findways(coins,amount,n)

