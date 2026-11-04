class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        n=len(matrix)
        c=len(matrix[0])
        l=0
        r=n*c-1

        while l<=r:
            m=(l+r)//2

            r1= m // c
            c1= m%c

            if matrix[r1][c1]==target:
                return True
            if matrix[r1][c1]<target:
                l=m+1
            else:
                r=m-1

        return False

        