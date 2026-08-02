class Solution:
    def temp(self,ans,result,nums,n,target,i):
        if(target<0 or i>=n):
            return
        if(target==0):
            print(ans)
            result.append(ans.copy())
            return
        
        #consider the first number
        ans.append(nums[i])
        self.temp(ans,result,nums,n,target-nums[i],i)
        ans.pop()
        #not consider the first number
        self.temp(ans,result,nums,n,target,i+1)

    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans=[]
        result=[]
        n=len(nums)
        self.temp(ans,result,nums,n,target,0)
        return(result)

        