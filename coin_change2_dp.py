class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
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

        t = [[0 for i in range(s+1)] for j in range(n+1)]
        #print(len(t),len(t[0]),t)

        for i in range(n+1):
            for j in range(amount+1):
                #print(i,j,amount)
                if j==0:
                    t[i][j]=1
                elif i==0:
                    t[i][j]=0
                else:
                    if j>=coins[i-1]:
                        t[i][j]=t[i][j-coins[i-1]]+t[i-1][j]
                    else:
                        t[i][j]=t[i-1][j]
        print(t)
        return t[n][amount]


