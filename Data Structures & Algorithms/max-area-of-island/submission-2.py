class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        a=0

        dirs=[[0,1],[1,0],[0,-1],[-1,0]]


        def bfs(r,c):
            q=deque()
            q.append([r,c])
            grid[r][c]="#"
            ct=1

            while q:
                r,c=q.popleft()
                for d in dirs:
                    nr=r+d[0]
                    nc=c+d[1]

                    if nr>=0 and nr<len(grid) and nc>=0 and nc<len(grid[0]) and grid[nr][nc]==1:
                        q.append([nr,nc])
                        grid[nr][nc]="#"
                        ct+=1
                    
            return ct



        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    a=max(a,bfs(i,j))
                    

        return a
        
        