class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        h={}
        mh=[]
        c=0
        res=[]

        for i in nums:
            if i not in h:
                h[i]=1
            else:
                h[i]+=1

                

        for i in h:
            heapq.heappush(mh,[h[i],i])
            c+=1

            if c>k:
                heapq.heappop(mh)

        

        for i,j in mh:
            res.append(j)

        return res




        