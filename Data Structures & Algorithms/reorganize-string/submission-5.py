class Solution:
    def reorganizeString(self, s: str) -> str:

        mh=[]
        h={}
        res=[]
        pre=None

        for i in s:
            if i not in h:
                h[i]=1
            else:
                h[i]+=1

        for i in h:
            heapq.heappush(mh,[-h[i],i])

        print(mh)
        
        while mh:
            c,ch=heapq.heappop(mh)
            res.append(ch)

            if pre:
                pc,pch=pre
                heapq.heappush(mh,[pc,pch])

            c+=1

            pre=(c,ch) if c<0 else None

        if len(res) != len(s):
            return ""
        
        return "".join(res)


