class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i=0
        j=len(nums)-1
        if(target>nums[j]):
            return(j+1)
        if(target<nums[i]):
            return(0)

        while(i<j):
            mid=(i+j)//2
            if(nums[mid]==target):
                return(mid)

            if(nums[mid]>target):
                j=mid
            else:
                i=mid+1
        print("i: ",i,"j: ",j)   
        return(i)
        