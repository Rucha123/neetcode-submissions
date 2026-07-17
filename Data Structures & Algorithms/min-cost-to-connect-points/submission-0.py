class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:


        adj=[]

        for i in range(len(points)):
            adj.append([])

        for i in range(len(points)):
            x1,y1=points[i]
            for j in range(i+1,len(points)):
                x2,y2=points[j]

                dist=abs(x1-x2)+abs(y1-y2)
                adj[i].append([dist,j])
                adj[j].append([dist,i])

        res=0
        visit=set()
        mh=[[0,0]]

        while len(visit)<len(points):
            c,i=heapq.heappop(mh)
            if i in visit:
                continue
            res+=c
            visit.add(i)

            for nc,nei in adj[i]:
                if nei not in visit:
                    heapq.heappush(mh,[nc,nei])

        return res




        