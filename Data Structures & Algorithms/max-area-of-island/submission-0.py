class Solution:
    def boundaryCondition(self,i,j,n,m):
        if(i<0 or j<0):
            return(False)
        if(i>=n or j>=m):
            return(False)
        return(True)
    
    def dfs(self,grid,visited,i,j,n,m):
        if not self.boundaryCondition(i, j, n, m) or visited[i][j] or grid[i][j] == 0:
            return 0
        
        visited[i][j] = 1
        # Sum 1 (current cell) + area of four directions
        return (1 
                + self.dfs(grid, visited, i+1, j, n, m)
                + self.dfs(grid, visited, i-1, j, n, m)
                + self.dfs(grid, visited, i, j+1, n, m)
                + self.dfs(grid, visited, i, j-1, n, m))

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])

        visited=[]
        for i in range(n):
            temp=[]
            for j in range(m):
                temp.append(0)
            visited.append(temp)
        
        maxTemp=0
        maxValue=0
        for i in range(n):
            for j in range(m):
                if(visited[i][j]==0 and grid[i][j]==1):
                    maxTemp=self.dfs(grid,visited,i,j,n,m)
                    maxValue=max(maxValue,maxTemp)
                    print('**************')
        
        return(maxValue)
        