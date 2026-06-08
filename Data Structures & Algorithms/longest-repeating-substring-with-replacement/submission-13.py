class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        h={}
        mf=0
        res=0
        j=0

        for i in range(len(s)):

            if s[i] not in h:
                h[s[i]]=1
            else:
                h[s[i]]+=1
            
            mf=max(mf,h[s[i]])

            while (i-j+1) - mf > k:
                h[s[j]]-=1
                j+=1
            res=max(res,(i-j+1))

        return res



        