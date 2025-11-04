class Solution:
    def floodFill(self, image, sr, sc, color):
        original = image[sr][sc]
        if original == color:
            return image  # No change needed

        def dfs(r, c):
            # If out of bounds or color not matching the original, skip
            if (r < 0 or r >= len(image) or 
                c < 0 or c >= len(image[0]) or 
                image[r][c] != original):
                return
            # Change color
            image[r][c] = color
            # Visit 4-directionally adjacent pixels
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        dfs(sr, sc)
        return image
