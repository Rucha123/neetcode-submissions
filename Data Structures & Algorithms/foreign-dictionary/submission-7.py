class Solution:
    def foreignDictionary(self, words: List[str]) -> str:

        adj={}
        ind={}

        for w in words:
            for c in w:
                adj[c]=[]
                ind[c]=0

        for i in range(len(words)-1):
            w1=words[i]
            w2=words[i+1]
            ml=min(len(w1),len(w2))
            if len(w1)>len(w2) and w1[:ml] == w2[:ml]:
                return ""
            for j in range(ml):
                if w1[j]!=w2[j]:
                    if w2[j] not in adj[w1[j]]:
                        adj[w1[j]].append(w2[j])
                        ind[w2[j]]+=1
                    break
        q=deque()
        res=[]
        for i in ind:
            if ind[i]==0:
                q.append(i)

        while q:
            cur=q.popleft()
            res.append(cur)
            for i in adj[cur]:
                ind[i]-=1
                if ind[i]==0:
                    q.append(i)

        if len(res)!=len(ind):
            return ""

        return "".join(res)
        