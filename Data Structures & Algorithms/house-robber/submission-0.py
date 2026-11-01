class Solution:
    def rob(self, nums: List[int]) -> int:

        p2=0
        p1=0

        for i in nums:
            tp=max(i+p2,p1)
            p2=p1
            p1=tp
          
     

        return p1

      
        