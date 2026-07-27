class Solution:
    def trap(self, height: List[int]) -> int:

        i=0
        j=len(height)-1
        ml=height[i]
        mr=height[j]
        res=0

        while i<j:

            if ml<mr:
                i+=1
                ml=max(ml,height[i])
                res+=ml-height[i]
            else:
                j-=1
                mr=max(mr,height[j])
                res+=mr-height[j]

        return res


        