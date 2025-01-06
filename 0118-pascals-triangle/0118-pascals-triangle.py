class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = []

        for i in range(numRows):
            # Start each row with 1
            row = [1] * (i + 1)
            # Fill in the middle elements
            for j in range(1, i):
                row[j] = result[i - 1][j - 1] + result[i - 1][j]
            # Append the row to the result
            result.append(row)

        return result