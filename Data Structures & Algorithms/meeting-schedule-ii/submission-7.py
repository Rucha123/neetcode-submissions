"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        st=[]
        ed=[]
        for i in intervals:
            st.append(i.start)
            ed.append(i.end)
        st.sort()
        ed.sort()

        print(st,ed)
        s=0
        e=0
        c=0
        res=0

        while s<len(intervals):
            if st[s]<ed[e]:
                s+=1
                c+=1
            else:
                e+=1
                c-=1
            res=max(res,c)
        
        return res
        