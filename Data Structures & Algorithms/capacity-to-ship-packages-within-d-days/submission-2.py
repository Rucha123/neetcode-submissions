class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l=max(weights)
        r=sum(weights)


        def canShip(m):
            d=1
            c=0

            for w in weights:
                if w+c>m:
                    d+=1
                    c=0
                c+=w

            return d<=days

        

        while l<=r:
            c=(l+r)//2
            if canShip(c):
                r=c-1
            else:
                l=c+1

        return l
        