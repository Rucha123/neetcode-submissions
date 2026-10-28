class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        h={}
        mh=[]
        res=[]

        for i in nums:
            if i not in h:
                h[i]=1
            else:
                h[i]+=1

        for i in h:
            heapq.heappush(mh,[h[i],i])

            if len(mh)>k:
                heapq.heappop(mh)

        for i in mh:
            res.append(i[1])

        return res

        
        