class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=sorted(set(nums))
        if(len(nums)==0):
            return(0)
        c=0
        maxTemp=0
        print(nums)
        for i in range(0,len(nums)-1):
            if(nums[i+1]-nums[i]==1):
                c+=1
            else:
                c=0
            maxTemp=max(maxTemp,c)
        return(maxTemp+1)
        