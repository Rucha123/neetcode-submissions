class Solution:
    def minWindow(self, s: str, t: str) -> str:

        h={}
        c=0
        st=""
        res=float("inf")

        for i in t:
            if i not in h:
                h[i]=1
            else:
                h[i]+=1


        i=j=0

        while i<=j and i<len(s):

            if (i!=j and c==len(h)) or j==len(s):
                if s[i] in h:
                    if h[s[i]]==0:
                        c-=1
                    h[s[i]]+=1
                i+=1

            else:
                if s[j] in h:
                    if h[s[j]]==1:
                        c+=1
                    h[s[j]]-=1
                j+=1

            if c==len(h):
                res=min(j-i,res)
                if res==j-i:
                    st=s[i:j]

        return st