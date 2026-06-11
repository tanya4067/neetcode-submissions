class Solution:
    def dfs(self,nums,temp,result,target,i):
        if(target<0):
            return
        if(target==0):
            # print(temp)
            if(temp not in result):
                result.append(temp[:])
            return
        
        for j in range(i,len(nums)):
            temp.append(nums[j])
            self.dfs(nums,temp,result,target-nums[j],j)
            temp.pop()

    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        temp=[]
        result=[]
        n=len(nums)

        for i in range(0,n):
            self.dfs(nums,temp,result,target,i)
        
        return(result)
        