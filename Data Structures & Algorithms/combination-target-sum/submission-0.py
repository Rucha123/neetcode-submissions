class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:


        res=[]
        nums.sort()

        def dfs(i,cur,t):
            if t==target:
                res.append(cur[:])
                return

            for j in range(i,len(nums)):
                if t+nums[j]>target:
                    return
                cur.append(nums[j])
                dfs(j,cur,t+nums[j])
                cur.pop()

        dfs(0,[],0)

        return res
        