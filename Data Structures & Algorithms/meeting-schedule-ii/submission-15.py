"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        h=defaultdict(int)
        for i in intervals:
            h[i.start]+=1
            h[i.end]-=1
        cs=0
        ms=0

        for i in sorted(h):
            cs+=h[i]
            ms=max(ms,cs)
            

        return ms


        