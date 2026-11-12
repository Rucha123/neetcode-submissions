class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:

        mh=[(grid[0][0],0,0)]
        visit=set()
        visit.add((0,0))

        while mh:
            t,r,c=heapq.heappop(mh)

            # if (r,c) in visit:
            #     continue
            
            # visit.add((r,c))
           
            if r==len(grid)-1 and c==len(grid[0])-1:
                return t

            for dr,dc in ((0,1),(0,-1),(1,0),(-1,0)):
                nr=r+dr
                nc=c+dc
                if nr>=0 and nc>=0 and nr<len(grid) and nc<len(grid[0]) and (nr,nc) not in visit:
                    mc=max(grid[nr][nc],t)
                    heapq.heappush(mh,(mc,nr,nc))
                    visit.add((nr,nc))




