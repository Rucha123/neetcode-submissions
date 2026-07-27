class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i=0
        j=len(heights)-1
        res=0

        while i<j:
            c=min(heights[i],heights[j])*(j-i)
            if heights[i]<heights[j]:
                i+=1
            else:
                j-=1
            res=max(res,c)

        return res
        