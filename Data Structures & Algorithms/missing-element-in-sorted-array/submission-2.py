class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        n=len(nums)
        i=nums[0]
        temp=[]
        c=0
        while(i<10000000000 and c<k):
            if(i not in nums):
                temp.append(i)
                c+=1
            i+=1
        print(temp)
        return(temp[k-1])

        