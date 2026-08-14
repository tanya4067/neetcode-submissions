class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n=len(nums)
        i=0
        ans=[]
        k=0
        while(i<n):
            if(nums[i] not in ans):
                ans.append(nums[i])
                k+=1
            i+=1
        
        for i in range(k):
            nums[i]=ans[i]
        return(k)
        