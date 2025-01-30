class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        for i in range(len(matrix)):
            row = matrix[i]
            for j in range(len(row)):
                if i > 0 and j > 0:
                    if matrix[i][j] != matrix[i-1][j-1]:
                        return False
                
        return True

        