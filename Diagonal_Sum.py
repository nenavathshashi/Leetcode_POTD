class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        primary_diagonal=0
        secondary_diagonal=0
        n=len(mat)
        for i in range(n):
            primary_diagonal+=mat[i][i]
            secondary_diagonal+=mat[i][n-i-1]
        diagonal_sum=primary_diagonal+secondary_diagonal
        return  diagonal_sum if n%2==0 else diagonal_sum-mat[n//2][n//2]
