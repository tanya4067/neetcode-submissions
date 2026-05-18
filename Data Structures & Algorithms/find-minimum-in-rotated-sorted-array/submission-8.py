class Solution:
    def findMin(self, nums: List[int]) -> int:
        n=len(nums)
        i=0
        j=n-1
        mid=0

        while(i<j):
            mid=(i+j)//2
            if(nums[mid]>nums[mid+1]):
                break
            
            if(nums[mid]>nums[i]):
                i=mid+1
            if(nums[mid]<nums[j]):
                j=mid
        
        if(i>=j):
            return(nums[0])
        print("i: ",i,"j: ",j,"mid: ",mid)
        if(mid<n-1):
            return(nums[mid+1])
        
        return(nums[0])