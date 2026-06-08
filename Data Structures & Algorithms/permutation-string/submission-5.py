class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Build the frequency of s1
        h = {}
        for ch in s1:
            h[ch] = h.get(ch, 0) + 1
        
        c = 0       # matched characters count
        i = 0       # left pointer
        
        for j in range(len(s2)):
            # If s2[j] is in s1 and still needed, increase match count
            if s2[j] in h and h[s2[j]] > 0:
                c += 1
            # Decrease the count in the map (even if it goes negative)
            if s2[j] in h:
                h[s2[j]] -= 1
            
            # Shrink window if window size > len(s1)
            if j >= len(s1):
                if s2[i] in h:
                    if h[s2[i]] >= 0:   # this char was part of s1
                        c -= 1
                    h[s2[i]] += 1
                i += 1
            
            # All characters matched
            if c == len(s1):
                return True
        
        return False
