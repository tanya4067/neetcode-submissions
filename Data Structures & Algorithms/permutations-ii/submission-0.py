class Solution:
    def swap(self,nums,i,j):
        if(nums[i]==nums[j]):
            return
        nums[i],nums[j]=nums[j],nums[i]

    def temp(self,result,nums,n,i):
        if(i>=n):
            if(nums not in result):
                result.append(nums.copy())
            return
        j=i
        while(j<n): 
            self.swap(nums,i,j)
            self.temp(result,nums,n,i+1)
            self.swap(nums,j,i)
            
            j+=1

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        result=[]

        self.temp(result,nums,n,0)
        return(result)