class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        h = {}
        res = 0

        l = 0
        maxf = 0
        for r in range(len(s)):
            if s[r] not in h:
                h[s[r]]=1
            else:
                h[s[r]]+=1
            maxf = max(maxf, h[s[r]])

            while (r - l + 1) - maxf > k:
                h[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)

        return res