class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        i=0
        j=0
        n=len(nums)
        currentSum=0
        maxSum=-1
        while(i<n):
            currentSum+=nums[i]
            maxSum=max(maxSum,currentSum)
            if(currentSum<0):
                j=i
                currentSum=0
            i+=1
        return(maxSum)


        