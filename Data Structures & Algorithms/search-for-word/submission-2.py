class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def dfs(r,c,i):

            if i==len(word)-1:
                return True
            board[r][c]="#"

            for dr,dc in ((0,1),(0,-1),(1,0),(-1,0)):
                nr=r+dr
                nc=c+dc

                if nr>=0 and nr<len(board) and nc>=0 and nc<len(board[0]) and board[nr][nc]==word[i+1] and board[nr][nc]!="#":
                    if dfs(nr,nc,i+1):
                        return True

            board[r][c]=word[i]

            return False

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c]==word[0] and dfs(r,c,0):
                    return True

        return False




        
        