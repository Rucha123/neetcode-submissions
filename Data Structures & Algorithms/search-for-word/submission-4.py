class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        dirs=[[0,1],[1,0],[0,-1],[-1,0]]


        def dfs(r,c,i):
            if i==len(word):
                return True
            if r<0 or c<0 or r>=len(board) or c>=len(board[0]) or word[i]!=board[r][c] or board[r][c]=="#":
                return False
            board[r][c]="#"
            res=dfs(r+1,c,i+1) or dfs(r-1,c,i+1) or dfs(r,c-1,i+1) or dfs(r,c+1,i+1)
            board[r][c]=word[i]

            return res

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i,j,0):
                    return True
        return False
        