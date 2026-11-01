class Solution:
    def reorganizeString(self, s: str) -> str:

        mh=[]
        res=[]
        h={}
        prev=None

        for i in s:
            if i not in h:
                h[i]=1
            else:
                h[i]+=1

        for i in h:
            heapq.heappush(mh,[-h[i],i])

        while mh:
            c,ch=heapq.heappop(mh)
            res.append(ch)

            if prev:
                pc,pch=prev
                heapq.heappush(mh,[pc,pch])

            c+=1
            
            if c<0:
                prev=(c,ch)
            else:
                prev=None
            
        if len(s) != len(res):
            return ""

        return "".join(res)
        