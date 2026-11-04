class Solution:

    def dfs(self,i,j,grid):
        grid[i][j]="0"

        for dr,dc in ((0,1),(0,-1),(1,0),(-1,0)):
            nr=dr+i
            nc=dc+j

            if nr>=0 and nc>=0 and nr<len(grid) and nc<len(grid[0]) and grid[nr][nc]=="1":
                self.dfs(nr,nc,grid)


        

    def numIslands(self, grid: List[List[str]]) -> int:

        c=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="1":
                    self.dfs(i,j,grid)
                    c+=1
        return c
        