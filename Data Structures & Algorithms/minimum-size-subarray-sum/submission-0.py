class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        i=j=0
        t=0
        res=float('inf')

        while j<len(nums):
            t+=nums[j]
            while t>=target:
                res=min(res,j-i+1)
                t-=nums[i]
                i+=1
            j+=1

        return 0 if res==float("inf") else res
        