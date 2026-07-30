class Solution:
    def temp(self,n,k,ans,result,i):
        if(len(ans)==k):
            print(ans)
            result.append(ans.copy())
            return
            
        for j in range(i,n):
            ans.append(j+1)
            self.temp(n,k,ans,result,j+1)
            ans.pop()
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans=[]
        result=[]

        self.temp(n,k,ans,result,0)

        return(result)
        