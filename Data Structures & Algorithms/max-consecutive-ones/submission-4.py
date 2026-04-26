class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        c=0
        nums.append(0)
        max_ans=0
        for i in nums:
            if(i==1):
                c+=1
            else:
                max_ans=max(max_ans,c)
                c=0
        return(max_ans)
        