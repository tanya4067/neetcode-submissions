class Solution:
    def dfs(self,nums,temp,result,i):
        if(i==len(nums)):
            if(temp not in result):
                result.append(temp[:])
            return
        
        # not include
        self.dfs(nums,temp,result,i+1)
        # to include
        temp.append(nums[i])
        self.dfs(nums,temp,result,i+1)
        temp.pop()

    def subsets(self, nums: List[int]) -> List[List[int]]:
        temp=[]
        result=[]
        n=len(nums)

        for i in range(n):
            self.dfs(nums,temp,result,i)
        
        return(result)
        