class Solution:
	def floodFill(self, image, sr, sc, newColor):
        rows, cols = len(image), len(image[0])
        originalColor = image[sr][sc]
        if originalColor == newColor:
            # No need to change
            return image
        
        def dfs(r, c):
            if (r<0 or r>=rows or c<0 or c>=cols or image[r][c]!=originalColor):
                return
            image[r][c] = newColor
            dfs(r+1, c) # down
            dfs(r-1, c) # up
            dfs(r, c+1) # right
            dfs(r, c-1) # left
            
        dfs(sr, sc)
        return image
