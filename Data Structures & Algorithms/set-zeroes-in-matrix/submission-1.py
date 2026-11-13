class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:


        n=len(matrix)
        m=len(matrix[0])
        fr=False
        fc=False

        for i in range(n):
            if matrix[i][0]==0:
                fc=True
        
        for j in range(m):
            if matrix[0][j]==0:
                fr=True

        for i in range(1,n):
            for j in range(1,m):
                if matrix[i][j]==0:
                    matrix[i][0]=0
                    matrix[0][j]=0

        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if fc:
            for i in range(n):
                matrix[i][0]=0

        
        if fr:
            for j in range(m):
                matrix[0][j]=0

        