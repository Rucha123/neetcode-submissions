class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        h={}
        l=0
        i=0
        res=0

        for j in range(len(s)):

            if s[j] in h:
                i=max(i,h[s[j]]+1)
                

            h[s[j]]=j
            res=max(j-i+1,res)

        return res

        