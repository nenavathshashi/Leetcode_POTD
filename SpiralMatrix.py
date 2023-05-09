class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row=len(matrix)
        column=len(matrix[0])
        answer=[]
        #visited matrix to mark the already visited cells
        visited=[[False for _ in range(column)] for _ in range(row)]


        #start by traversing first by updating cell value by (old+0,old+1) ->
        #take a turn when you exceed the column by updating the cell by (old+1,old+0)
        #similarly have to take regular turnings
        # done by using the dr and dc arrays


        dr=[0,1,0,-1]
        dc=[1,0,-1,0]
        starting_x=0
        starting_y=0

        #starting index of dr and dc array

        start=0
        #instead of two for loops can be written as a single loop

        for i in range(row*column):
            answer.append(matrix[starting_x][starting_y])
            visited[starting_x][starting_y]=True
            new_x=starting_x+dr[start]
            new_y=starting_y+dc[start]

            #check if out of bounds or already visited
            if new_x>=0 and new_x<row and new_y>=0 and new_y<column and visited[new_x][new_y]==False:
                starting_x=new_x
                starting_y=new_y
            else:
                #take turns
                start=(start+1)%4
                starting_x+=dr[start]
                starting_y+=dc[start]
        return answer
