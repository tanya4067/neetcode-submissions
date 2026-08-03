class Solution:
    def dfs(self,ans,nums,n,i):
        if(i==n):
            ans.append(nums[:])
            return
       
        for j in range(i,n):
            nums[i],nums[j]=nums[j],nums[i]
            self.dfs(ans,nums,n,i+1)
            nums[i],nums[j]=nums[j],nums[i]
        
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        n=len(nums)

        self.dfs(ans,nums,n,0)

        return(ans)
        