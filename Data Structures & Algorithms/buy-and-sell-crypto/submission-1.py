class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        i=0
        j=1
        mxp=0

        while j<len(prices):
            if prices[i]<prices[j]:
                pr=prices[j]-prices[i]
                mxp=max(mxp,pr)
            else:
                i=j

            j+=1

        return mxp


        