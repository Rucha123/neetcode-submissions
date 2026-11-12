class Solution:
    def solve(self, board: List[List[str]]) -> None:
        q=deque()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if (i==0 or j==0 or i==len(board)-1 or j==len(board[0])-1) and board[i][j]=="O":
                    q.append((i,j))
                    board[i][j]="s"

        while q:
            r,c=q.popleft()
            for dr,dc in ((0,1),(0,-1),(-1,0),(1,0)):
                nr=r+dr
                nc=c+dc
                if nr>0 and nc>0 and nr<len(board)-1 and nc<len(board[0])-1 and board[nr][nc]=="O":
                    q.append((nr,nc))
                    board[nr][nc]="s"
                    

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]=="O":
                    board[i][j]="X"
                elif board[i][j]=="s":
                    board[i][j]="O"
        