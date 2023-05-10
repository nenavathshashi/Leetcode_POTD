class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans=[[0 for _ in range(n)] for _ in range(n)]
        dr=[0,1,0,-1]
        dc=[1,0,-1,0]
        x=0
        y=0
        di=0
        for i in range(n*n):
            ans[x][y]=i+1
            # print(ans[x][y])
            new_x=x+dr[di]
            new_y=y+dc[di]
            if new_x>=0 and new_x<n and new_y>=0 and new_y<n and ans[new_x][new_y]==0:
                x=new_x
                y=new_y
            else:
                di=(di+1)%4
                x=x+dr[di]
                y=y+dc[di]
        return ans
