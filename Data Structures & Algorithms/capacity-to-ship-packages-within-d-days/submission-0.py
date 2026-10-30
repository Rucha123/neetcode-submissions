class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        l=max(weights)
        r=sum(weights)

        def canShip(cap):
            d=1
            c=0

            for w in weights:
                if w+c>cap:
                    d+=1
                    c=0
                c+=w

            return d<=days

        while l<=r:
            cp = (l+r)//2
            if canShip(cp):
                r= cp - 1
            else:
                l = cp + 1

        return l
            


        