class Solution:
    def dfs(self,nums,target,temp,ans,i):
        if(target==0):
            temp=sorted(temp)
            if(temp not in ans):
                ans.append(list(temp))
            return
            
        
        if(target<0 or i>=len(nums)):
            return
        
        temp.append(nums[i])
        
        self.dfs(nums,target-nums[i],temp,ans,i)

        temp.pop()
        self.dfs(nums,target,temp,ans,i+1)


    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        n=len(nums)
        temp=[]
        ans=[]
        
        self.dfs(nums,target,temp,ans,0)
        
        print("ans ",ans)
        
        return(ans)
        