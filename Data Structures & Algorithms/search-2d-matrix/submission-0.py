class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n=len(matrix)
        m=len(matrix[0])

        for i in range(0,n):
            last=matrix[i][m-1]
            if(target<=last):
                for j in range(0,m):
                    if(matrix[i][j]==target):
                        return(True)
        return(False)
        