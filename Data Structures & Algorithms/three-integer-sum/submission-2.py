class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            s=i+1
            e=len(nums)-1

            while s<e:
                su=nums[i]+nums[s]+nums[e]
                if su==0:
                    res.append((nums[i],nums[s],nums[e]))
                    s+=1
                    e-=1
                    while s < e and nums[s] == nums[s-1]:
                        s += 1

                    # Skip duplicate third numbers
                    while s < e and nums[e] == nums[e+1]:
                        e -= 1
                
                elif su<0:
                    s+=1
                else:
                    e-=1

        return res
        