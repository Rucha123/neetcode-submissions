class Solution:
    def reorganizeString(self, s: str) -> str:
        h={}
        m=-float("inf")
        res=[]
        res1=[]
        prev=None

        for i in s:
            if i not in h:
                h[i]=1
            else:
                h[i]+=1
        
        for i in h:
            heapq.heappush(res,[-h[i],i])

        while res:
            c,ch=heapq.heappop(res)
            res1.append(ch)

            if prev:
                pc,pch=prev
                heapq.heappush(res,[pc,pch])
            c+=1
            
            if c<0:
                prev=(c,ch)
            else:
                prev=None

        if len(s) != len(res1):
            return ""

        return "".join(res1)
        
        