"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        eve=[]
        cs=0
        ms=0

        for i in intervals:
            eve.append((i.start,1))
            eve.append((i.end,-1))

        eve.sort()

        for i,j in eve:
            cs+=j
            ms=max(cs,ms)

        return ms
            

        