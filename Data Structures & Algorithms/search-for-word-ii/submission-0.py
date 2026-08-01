class TrieNode:

    def __init__(self):
        self.child={}
        self.word=None



class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        root=TrieNode()
        res=[]

        for word in words:
            cur=root

            for ch in word:
                if ch not in cur.child:
                    cur.child[ch]=TrieNode()
                cur=cur.child[ch]
            cur.word=word

        def dfs(i,j,node):
            ch=board[i][j]
            if ch not in node.child:
                return
            nxt=node.child[ch]
            if nxt.word is not None:
                res.append(nxt.word)
                nxt.word=None
            board[i][j]="#"

            for dr,dc in ((0,1),(0,-1),(-1,0),(1,0)):
                nr=i+dr
                nc=j+dc
                if nr>=0 and nr<len(board) and nc>=0 and nc<len(board[0]) and board[nr][nc]!="#":
                    dfs(nr,nc,nxt)
            board[i][j]=ch

            if not nxt.child:
                del node.child[ch]





        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(i,j,root)
        return res



        