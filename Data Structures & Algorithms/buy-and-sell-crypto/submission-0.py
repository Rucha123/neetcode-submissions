class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        mp=float("-inf")
        mb=float("inf")

        for i in range(len(prices)):
            mb=min(mb,prices[i])
            mp=max(mp,prices[i]-mb)

        return mp

            
            




            
        