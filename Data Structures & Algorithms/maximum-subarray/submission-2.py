class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        i=0
        n=len(nums)
        currSum=0
        maxSum=-1
        while(i<n):
            currSum+=nums[i]
            maxSum=max(maxSum,currSum)
            if(currSum<0):
                currSum=0
            i+=1
        return(maxSum)
        