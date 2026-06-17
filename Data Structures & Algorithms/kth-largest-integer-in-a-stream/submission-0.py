import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.mh=[]
        self.k=k
        t=[]
        for i in nums:
            heapq.heappush(self.mh,i)
            k-=1

            if k<0:
                heapq.heappop(self.mh)

        
    def add(self, val: int) -> int:

        heapq.heappush(self.mh,val)

        if len(self.mh)>self.k:
            heapq.heappop(self.mh)

        return self.mh[0]


        
        
