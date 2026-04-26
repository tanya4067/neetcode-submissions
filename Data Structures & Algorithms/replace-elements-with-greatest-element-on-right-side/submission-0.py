class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        ans=[]
        n=len(arr)
        maxValue=arr[n-1]
        for i in range(0,n):
            ans.append(maxValue)
            maxValue=max(maxValue,arr[n-i-1])
        
        ans[0]=-1
        
        return(ans[::-1])
        