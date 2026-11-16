from collections import defaultdict
class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:

        st=defaultdict(int)
        end=defaultdict(int)
        cs=0
        ms=0

        for i in intervals:
          
            st[i[0]]+=1
            end[i[1]]-=1

        for i in sorted(set(st) | set(end)):
            cs+=st[i]
            ms=max(cs,ms)
            cs+=end[i]

        return ms
        
