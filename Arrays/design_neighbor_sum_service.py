from typing import List

class NeighborSum:
    '''
    You are given a n x n 2D array grid containing distinct elements in the range [0, n2 - 1].

    Implement the NeighborSum class:

    NeighborSum(int [][]grid) initializes the object.
    int adjacentSum(int value) returns the sum of elements which are adjacent neighbors of value, that is either to the top, left, right, or bottom of value in grid.
    int diagonalSum(int value) returns the sum of elements which are diagonal neighbors of value, that is either to the top-left, top-right, bottom-left, or bottom-right of value in grid.

    '''
    def __init__(self, grid: List[List[int]]):
        self.grid = grid
        self.n = len(grid)
        size = self.n * self.n
        self.row = [0] * size
        self.col = [0] * size
        
        for r in range(self.n):
            for c in range(self.n):
                v = grid[r][c]
                self.row[v] = r
                self.col[v] = c

    def adjacentSum(self, value: int) -> int:
        r, c = self.row[value], self.col[value]
        res = 0
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < self.n and 0 <= nc < self.n:
                res += self.grid[nr][nc]
        return res

    def diagonalSum(self, value: int) -> int:
        r, c = self.row[value], self.col[value]
        res = 0
        for dr, dc in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < self.n and 0 <= nc < self.n:
                res += self.grid[nr][nc]
        return res

# Your NeighborSum object will be instantiated and called as such:
grid = [[0,1,2],[3,4,5],[6,7,8]]
value = 4
obj = NeighborSum(grid)
param_1 = obj.adjacentSum(value)
print(param_1) # Expected output: 16 (1+3+5+7)
param_2 = obj.diagonalSum(value)
print(param_2) # Expected output: 16 (0+2+6+8)