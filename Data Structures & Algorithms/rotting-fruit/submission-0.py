class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        q=deque()
        dir=[[0,1],[1,0],[0,-1],[-1,0]]
        t=0
        f=0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==2:
                    q.append([i,j])
                    grid[i][j]="#"
                elif grid[i][j]==1:
                    f+=1

        while f>0 and q:
            t+=1
            for i in range(len(q)):
                r,c = q.popleft()
                
                for d in dir:
                    nr=r+d[0]
                    nc=c+d[1]

                    if nr>=0 and nr<len(grid) and nc>=0 and nc<len(grid[0]) and grid[nr][nc]==1:
                        q.append([nr,nc])
                        grid[nr][nc]="#"
                        f-=1

        return t if f==0 else -1
        