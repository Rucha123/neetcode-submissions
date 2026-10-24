class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:


        l=1
        r=res=max(piles)

        while l<=r:
            k=(l+r)//2
            t=0
            for i in piles:
                t+=math.ceil(i/k)

            if t<=h:
                res=k
                r=k-1
            else:
                l=k+1

            

        return res
        