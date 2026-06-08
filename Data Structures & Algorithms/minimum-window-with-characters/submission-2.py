class Solution:
    def minWindow(self, s: str, t: str) -> str:
        h = {}
        res = float("inf")
        c = 0
        st = ""

        for ch in t:
            h[ch] = h.get(ch, 0) + 1

        i = j = 0

        while j < len(s):
            if s[j] in h:
                h[s[j]] -= 1
                if h[s[j]] == 0:
                    c += 1
            j += 1

            while c == len(h):
                if j - i < res:
                    res = j - i
                    st = s[i:j]

                if s[i] in h:
                    if h[s[i]] == 0:
                        c -= 1
                    h[s[i]] += 1
                i += 1

        return st
