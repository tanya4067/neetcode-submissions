class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i=0
        j=1
        n=len(prices)
        max_temp=0
        while(i<n and j<n):
            if(prices[j]<prices[i]):
                
                i+=1
            else:
                max_temp=max(max_temp,prices[j]-prices[i])
                j+=1

        
        return(max_temp)
        