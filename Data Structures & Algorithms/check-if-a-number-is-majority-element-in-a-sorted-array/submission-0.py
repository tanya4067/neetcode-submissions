class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        n=len(nums)
        if(target not in nums):
            return(False)
        
        mapTemp={}
        for i in range(n):
            if(nums[i] in mapTemp):
                mapTemp[nums[i]]+=1
            else:
                mapTemp[nums[i]]=1
        
        maxAns=mapTemp[target]
        if(maxAns>n//2):
            return(True)
        return(False)
        