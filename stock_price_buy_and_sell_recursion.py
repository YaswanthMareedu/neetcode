class Solution:
    def maxProfit(self, prices: List[int],min_val=99999999,max_profit=0) -> int:
        if len(prices)==0:
            return max_profit
        if prices[0]<min_val:
            min_val = prices[0]
        
        if prices[0]-min_val>max_profit:
            max_profit=prices[0]-min_val

        return self.maxProfit(prices[1:],min_val,max_profit)
        
        
