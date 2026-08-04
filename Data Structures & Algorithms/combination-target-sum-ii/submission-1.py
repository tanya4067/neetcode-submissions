class Solution:
    def temp(self,ans,result,candidates,n,target,i,dp):
        if(target<0):
            return
        
        if(target==0):
            if(ans not in result):
                result.append(ans.copy())
            return
        for j in range(i,n):
            if j > i and candidates[j] == candidates[j-1]:
                continue
            ans.append(candidates[j])
            self.temp(ans,result,candidates,n,target-candidates[j],j+1,dp)
            ans.pop()

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]
        result=[]
        n=len(candidates)
        candidates=sorted(candidates)
        dp=[]
        self.temp(ans,result,candidates,n,target,0,dp)

        return(result)
        