class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans=[]
        n=len(nums)
        for i in range(n):
            ans.append(nums[i]*nums[i])
        return(sorted(ans))
        