"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        mh=[]
        intervals.sort(key=lambda x:x.start)

        for i in intervals:
            if mh and mh[0]<=i.start:
                heapq.heappop(mh)

            heapq.heappush(mh,i.end)

        return len(mh)

        