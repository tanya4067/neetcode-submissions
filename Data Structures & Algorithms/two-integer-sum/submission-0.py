class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp={}
        ans=[]
        for i in range(0,len(nums)):
            if(nums[i] in temp):
                ans.append(temp[nums[i]])
                ans.append(i)
                break
            else:
                temp[target-nums[i]]=i
        return(ans)

        