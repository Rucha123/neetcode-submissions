class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q=deque()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==0:
                    q.append((i,j))

        while q:
            r,c=q.popleft()

            for dr,dc in ((0,1),(1,0),(-1,0),(0,-1)):
                nr=dr+r
                nc=dc+c
                if nr>=0 and nc>=0 and nr<len(grid) and nc<len(grid[0]) and grid[nr][nc]==2147483647:
                    grid[nr][nc]=grid[r][c]+1
                    q.append((nr,nc))
        