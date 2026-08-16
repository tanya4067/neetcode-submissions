class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        totalSum=0
        for i in nums:
            totalSum+=i

        left=0
        right=0
        for i in range(0,len(nums)):
            right=totalSum-left-nums[i]
            if(left==right):
                return(i)
            # print("left: ",left," right: ",right)
            left+=nums[i]
        return(-1)
        