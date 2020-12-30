"""
Given an m x n matrix of non-negative integers representing the height of each unit cell in a continent, the "Pacific ocean" touches the left and top edges of the matrix and the "Atlantic ocean" touches the right and bottom edges.

Water can only flow in four directions (up, down, left, or right) from a cell to another one with height equal or lower.

Find the list of grid coordinates where water can flow to both the Pacific and Atlantic ocean.

Note:

The order of returned grid coordinates does not matter.
Both m and n are less than 150.
 

Example:

Given the following 5x5 matrix:

  Pacific ~   ~   ~   ~   ~ 
       ~  1   2   2   3  (5) *
       ~  3   2   3  (4) (4) *
       ~  2   4  (5)  3   1  *
       ~ (6) (7)  1   4   5  *
       ~ (5)  1   1   2   4  *
          *   *   *   *   * Atlantic

Return:

[[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (positions with parentheses in above matrix).
"""


class Solution:

    def dfs(self, block, r, c, rb, cb, check, prev):
        if r<0 or c<0 or r > (rb-1) or c > (cb-1):
            return
        if check[r][c] == -1:
            return
        if block[r][c] < prev:
            return 
        
        check[r][c] = -1
        self.dfs(block, r+1, c, rb, cb, check, block[r][c])
        self.dfs(block, r-1, c, rb, cb, check, block[r][c])
        self.dfs(block, r, c+1, rb, cb, check, block[r][c])
        self.dfs(block, r, c-1, rb, cb, check, block[r][c])
        
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        ans = []
        # Edge Case
        if len(matrix) == 0:
            return ans
        rows = len(matrix)
        columns = len(matrix[0])
        pac = [[0]*columns for i in range(rows)]
        atl = [[0]*columns for i in range(rows)]
        
        # Pacific = 1st row, 1st column
        for i in range(columns):
            self.dfs(matrix, 0, i, rows, columns, pac, float("-inf"))
        for i in range(rows):
            self.dfs(matrix, i, 0, rows, columns, pac, float("-inf"))
            
        # Atlantic = last row, last column
        for i in range(columns):
            self.dfs(matrix, rows-1, i, rows, columns, atl, float("-inf"))
        for i in range(rows):
            self.dfs(matrix, i, columns-1, rows, columns, atl, float("-inf"))
        for m in range(rows):
            for n in range(columns):
                if pac[m][n] == -1 and atl[m][n] == -1:
                    ans.append([m,n])
        return ans
        
        
