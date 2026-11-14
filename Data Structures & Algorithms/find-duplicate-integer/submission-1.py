class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        # h={}

        # for i in nums:
        #     if i not in h:
        #         h[i]=1
        #     else:
        #         h[i]+=1

        # for i in h:
        #     if h[i]>1:
        #         return i 

        nums.sort()
        i=1
 
        while i<len(nums):
            if nums[i]!=nums[i-1]:
                i+=1
            else:
                return nums[i]
        