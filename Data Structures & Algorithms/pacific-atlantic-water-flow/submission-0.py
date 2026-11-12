class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        p=set()
        a=set()
        res=[]

        def dfs(r,c,visit):
            if (r,c) in visit:
                return
            visit.add((r,c))
            
            for dr,dc in ((0,1),(0,-1),(-1,0),(1,0)):
                nr=r+dr
                nc=c+dc
                if nr>=0 and nr<len(heights) and nc>=0 and nc<len(heights[0]) and heights[nr][nc]>=heights[r][c]:
                    dfs(nr,nc,visit)



        #first row and column
        for i in range(len(heights)):
            dfs(i,0,p)
        for j in range(len(heights[0])):
            dfs(0,j,p)
        
        #last row and column
        for i in range(len(heights)):
            dfs(i,len(heights[0])-1,a)

        for j in range(len(heights[0])):
            dfs(len(heights)-1,j,a)

        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if (i,j) in p and (i,j) in a:
                    res.append([i,j])

        return res