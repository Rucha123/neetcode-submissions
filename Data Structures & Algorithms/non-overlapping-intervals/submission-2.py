class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort()

        res=0
        pe=intervals[0][1]
        
        for s,e in intervals[1:]:
            if s>=pe:
                pe=e
            else:
                res+=1
                pe=min(pe,e)

        return res
