class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        MIN = float('inf')
        profit = 0
        for i in prices:
            if i < MIN:
                MIN = i
            
            if profit < i - MIN:
                profit = i - MIN
        
        return profit
