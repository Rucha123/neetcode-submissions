class Solution:


    def helper(self,nums):
        p2=0
        p1=0

        for i in nums:
            tp=max(i+p2,p1)
            p2=p1
            p1=tp

        return p1


    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]

        return max(self.helper(nums[1:]),self.helper(nums[:-1]))
        