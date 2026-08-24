class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        even=[]
        odd=[]
        n=len(nums)

        for i in range(n):
            if(nums[i]%2==0):
                even.append(nums[i])
            else:
                odd.append(nums[i])
        ans=[]
        for i in even:
            ans.append(i)
        for j in odd:
            ans.append(j)

        return(ans)
        