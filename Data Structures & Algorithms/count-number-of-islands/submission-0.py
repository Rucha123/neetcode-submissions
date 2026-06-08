class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        c=0

        def bfs(r,c,grid):

            dirs=[[1,0],[0,1],[0,-1],[-1,0]]

            q=deque()
            q.append([r,c])
            while q:
                r,c=q.popleft()

                for d in dirs:
                    nr=r+d[0]
                    nc=c+d[1]

                    if nr>=0 and nr<len(grid) and nc>=0 and nc<len(grid[0]) and grid[nr][nc]!="#" and grid[nr][nc]=="1":
                        q.append([nr,nc])
                        grid[nr][nc]="#"



        for i in range(len(grid)):
            for j in range(len(grid[0])):

                if grid[i][j]=="1":
                    grid[i][j]="#"
                    bfs(i,j,grid)
                    c+=1

        return c
        