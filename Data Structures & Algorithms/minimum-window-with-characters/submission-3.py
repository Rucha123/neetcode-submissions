class Solution:
    def minWindow(self, s: str, t: str) -> str:

        h={}
        st=""
        res=float("inf")
        ct=0

        for c in t:
            if c not in h:
                h[c]=1
            else:
                h[c]+=1

        i=j=0

        while j<len(s):
            if s[j] in h:
                h[s[j]]-=1
                if h[s[j]]==0:
                    ct+=1
            j+=1

            while ct==len(h):
                if j-i<res:
                    res=j-i
                    st=s[i:j]

                if s[i] in h:
                    if h[s[i]]==0:
                        ct-=1
                    h[s[i]]+=1
                i+=1


        return st



        