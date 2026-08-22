class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        n=len(nums)
        maxAns,maxSum=-1,-1
        for i in range(0,n-1):
            for j in range(i+1,n):
                maxSum=nums[i]+nums[j]
                if(maxSum<k):
                    maxAns=max(maxAns,maxSum)
        return(maxAns)
        