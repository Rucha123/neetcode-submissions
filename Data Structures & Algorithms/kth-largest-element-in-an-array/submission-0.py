class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h=[]
        for i in nums:
            heapq.heappush(h,i)
            k-=1
            if k<0:
                heapq.heappop(h)

        return heapq.heappop(h)






        