class Solution:
    def jump(self, nums: List[int]) -> int:

        j=0
        f=0
        e=0
        for i in range(len(nums)-1):
            f=max(f,i+nums[i])

            if i==e:
                j+=1
                e=f

        return j
         
                    


                
                
                

        