class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:

        h={}
        h1={}
        res=[]
        max_c=0
        best_p=None

        for i in range(len(username)):
            res.append([username[i],timestamp[i],website[i]])

        res.sort(key=lambda x:x[1])

        for u,t,w in res:
            if u not in h:
                h[u]=[w]
            else:
                h[u].append(w)

        for u in h:
            sites=h[u]
            seen=set()
            n=len(sites)
            for i in range(n-2):
                for j in range(i+1,n-1):
                    for k in range(j+1,n):
                        p=(sites[i],sites[j],sites[k])
                        seen.add(p)

            for p in seen:
                if p not in h1:
                    h1[p]=1
                else:
                    h1[p]+=1

        print(h1)

        for p in h1:
            c=h1[p]
            if c>max_c:
                max_c=c
                best_p=p
            elif c==max_c:
                if best_p is None or p<best_p:
                    best_p=p

        return list(best_p)


        