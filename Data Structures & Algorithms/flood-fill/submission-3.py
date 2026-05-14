class Solution:
    def dfs(self,image,visited,sr,sc,color,x):
        n=len(image)
        m=len(image[0])
        if(visited[sr][sc]==0 and image[sr][sc] == x):
            visited[sr][sc]=1
            image[sr][sc]=color

            if(self.boundaryCondition(sr+1,sc,n,m)):
                self.dfs(image,visited,sr+1,sc,color,x)
            
            if(self.boundaryCondition(sr,sc+1,n,m)):
                self.dfs(image,visited,sr,sc+1,color,x)
            
            if(self.boundaryCondition(sr-1,sc,n,m)):
                self.dfs(image,visited,sr-1,sc,color,x)
            
            if(self.boundaryCondition(sr,sc-1,n,m)):
                self.dfs(image,visited,sr,sc-1,color,x)
        
        return
            

    def boundaryCondition(self,i,j,n,m):
        if(i<0 or j<0):
            return(False)
        
        if(i>=n or j>=m):
            return(False)

        return(True)
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        n=len(image)
        m=len(image[0])

        visited=[]

        for i in range(n):
            ans=[]
            for j in range(m):
                ans.append(0)
            visited.append(ans)
        
        x=image[sr][sc]
        
        if(visited[sr][sc]==0):
            self.dfs(image,visited,sr,sc,color,x)
        
        return(image)


        