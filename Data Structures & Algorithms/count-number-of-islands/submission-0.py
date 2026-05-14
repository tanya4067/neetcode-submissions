class Solution:
    
    def boundaryCondition(self,n,m,i,j):
        if(i>=n or j>=m):
            return(False)
        if(i<0 or j<0):
            return(False)
        
        return(True)
    def dfs(self,grid,visited,i,j):
        n=len(grid)
        m=len(grid[0])  
        if(visited[i][j]==0 and grid[i][j]=="1"):
            visited[i][j]=1
            if(self.boundaryCondition(n,m,i+1,j)):
                self.dfs(grid,visited,i+1,j)
            if(self.boundaryCondition(n,m,i,j+1)):
                self.dfs(grid,visited,i,j+1)
            if(self.boundaryCondition(n,m,i-1,j)):
                self.dfs(grid,visited,i-1,j)
            if(self.boundaryCondition(n,m,i,j-1)):
                self.dfs(grid,visited,i,j-1)
            
            
        return
    def numIslands(self, grid: List[List[str]]) -> int:
        n=len(grid)
        m=len(grid[0])

        visited=[]
        for i in range(0,n):
            temp=[]
            for j in range(0,m):
                temp.append(0)
            visited.append(temp)
        
        count=0
        for i in range(n):
            for j in range(m):
                if(grid[i][j]=="1" and visited[i][j]==0):
                    # print("i: ",i,"j: ",j)
                    self.dfs(grid,visited,i,j)
                    count+=1
        return(count)
                

        