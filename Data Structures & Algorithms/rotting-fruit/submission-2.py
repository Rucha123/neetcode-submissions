class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        f=0
        q=deque()
        t=0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    f+=1
                elif grid[i][j]==2:
                    q.append((i,j))

        while q and f>0:
            t+=1
            for i in range(len(q)):
                r,c=q.popleft()

                for dr,dc in ((0,1),(0,-1),(1,0),(-1,0)):
                    nr=dr+r
                    nc=dc+c

                    if nr>=0 and nc>=0 and nr<len(grid) and nc<len(grid[0]) and grid[nr][nc]==1:
                        q.append((nr,nc))
                        grid[nr][nc]=2
                        f-=1

        return t if f==0 else -1


                
        