class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q=deque()
        res=[]
        i=j=0

        while j<len(nums):

            while q and nums[q[-1]]<nums[j]:
                q.pop()
            q.append(j)

            if j-k+1 > q[0]:
                q.popleft()


            if (j-k+1)>=0:
                res.append(nums[q[0]])
                i+=1

            j+=1

        return res

            
        