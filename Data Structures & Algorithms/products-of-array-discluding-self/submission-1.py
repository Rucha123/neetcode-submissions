class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p=1

        arr=[1]*len(nums)

        for i in range(len(nums)):
            arr[i]=arr[i]*p
            p=p*nums[i]
        
        p1=1

        for i in range(len(nums)-1,-1,-1):
            arr[i]=arr[i]*p1
            p1=p1*nums[i]

        return arr