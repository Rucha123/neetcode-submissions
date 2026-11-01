class Solution:
    def minWindow(self, s: str, t: str) -> str:

        h={}
        st=""
        res=float("inf")

        for i in t:
            if i not in h:
                h[i]=1
            else:
                h[i]+=1

        j=0
        i=0
        m=0

        while j<len(s):
            if s[j] in h:
                h[s[j]]-=1
                if h[s[j]]==0:
                    m+=1
            j+=1

            while m==len(h):
                if j-i<res:
                    res=j-i
                    st=s[i:j]
                
                if s[i] in h:
                    if h[s[i]]==0:
                        m-=1
                    h[s[i]]+=1

                i+=1

        return st


        