"""
Given N x M character matrix A of O's and X's, where O = white, X = black.

Return the number of black shapes. A black shape consists of one or more adjacent X's (diagonals not included)



Input Format:

    The First and only argument is a N x M character matrix.
Output Format:

    Return a single integer denoting number of black shapes.
Constraints:

    1 <= N,M <= 1000
    A[i][j] = 'X' or 'O'
Example:

Input 1:
    A = [ OOOXOOO
          OOXXOXO
          OXOOOXO  ]
Output 1:
    3
Explanation:
    3 shapes are  :
    (i)    X
         X X
    (ii)
          X
    (iii)
          X
          X
"""


class Solution:
    # @param A : list of strings
    # @return an integer
    def black(self, A):
        
        n = len(A)
        m = len(A[0])
        
        def is_valid(r, c):
            if 0<=r<n and 0<=c<m:
                return True
            return False
        res = 0
        visited = [[False for i in range(m)] for h in range(n)]
        def dfs(i, j):
            if A[i][j] == "X" and visited[i][j] == False:
                    visited[i][j] = True
                    for k in [(1,0), (0, 1), (-1,0), (0, -1)]:
                        if is_valid(i+k[0], j+k[1]):
                            dfs(i+k[0], j+k[1])
                    return 1
            return 0
        for x in range(n):
            for y in range(m):
                
                if dfs(x, y)==1:
                    res += 1
        return res
