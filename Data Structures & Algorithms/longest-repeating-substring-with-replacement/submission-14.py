class Solution:
    def characterReplacement(self, s: str, k: int) -> int:


        i=0
        h={}
        mf=0
        res=0


        for j in range(len(s)):

            if s[j] not in h:
                h[s[j]]=1
            else:
                h[s[j]]+=1

            mf=max(mf,h[s[j]])

            while (j-i+1) - mf > k:
                h[s[i]]-=1
                i+=1
            res=max(res,j-i+1)

        return res
        