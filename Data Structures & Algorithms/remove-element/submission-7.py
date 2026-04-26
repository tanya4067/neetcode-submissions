class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        c=0
        n=len(nums)

        while val in nums:
            nums.remove(val)
            c+=1
        
        return (n-c)


        