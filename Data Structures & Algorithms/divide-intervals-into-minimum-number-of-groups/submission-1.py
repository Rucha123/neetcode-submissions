class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        
        eve=[]
        cs=0
        ms=0


        for l,r in intervals:
            eve.append([l,1])
            eve.append([r,-1])

        eve.sort(key=lambda x:(x[0],-x[1]))

        for i,j in eve:
            cs+=j
            ms=max(cs,ms)

        return ms



