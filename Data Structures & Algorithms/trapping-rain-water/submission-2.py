class Solution:
    def trap(self, height: List[int]) -> int:

        l=0
        r=len(height)-1
        ml=height[l]
        mr=height[r]

        res=0

        while l<r:

            if ml<mr:
                l+=1
                ml=max(ml,height[l])
                res+=ml-height[l]
            else:
                r-=1
                mr=max(mr,height[r])
                res+=mr-height[r]

        return res
           