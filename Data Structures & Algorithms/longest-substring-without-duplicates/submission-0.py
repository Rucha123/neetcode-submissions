class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        h={}
        i=0
        res=0
        for j in range(len(s)):
            if s[j] in h:
                i=max(h[s[j]]+1,i)
            h[s[j]]=j

            res=max(res,j-i+1)

        return res



        