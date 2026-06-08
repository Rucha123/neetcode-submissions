class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        s=0
        e=len(nums)-1
        i=0
        while i<=e:
            if nums[i]==0:
                nums[s],nums[i]=nums[i],nums[s]
                s+=1
                i+=1
            elif nums[i]==1:
                i+=1
            else:
                nums[i],nums[e]=nums[e],nums[i]
                e-=1
        