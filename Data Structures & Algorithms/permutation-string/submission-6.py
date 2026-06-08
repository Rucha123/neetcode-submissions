class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Build the frequency of s1
        h = {}
        for ch in s1:
            h[ch] = h.get(ch, 0) + 1
        
        c = 0       # matched characters count
        i = 0       # left pointer

        for j in range(len(s2)):
            if s2[j] in h and h[s2[j]]>0:
                c+=1
            if s2[j] in h:
                h[s2[j]]-=1

            if j>=len(s1):
                if s2[i] in h:
                    if h[s2[i]]>=0:
                        c-=1
                    h[s2[i]]+=1
                i+=1

            if c == len(s1):
                return True
        
        return False
