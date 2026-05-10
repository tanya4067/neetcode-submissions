class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i=0
        j=len(heights)-1
        maxTemp=0

        while(i<j):
            curr_min=min(heights[i],heights[j])
            maxTemp=max(maxTemp,curr_min*(j-i))

            if(heights[i]<heights[j]):
                i+=1
            else:
                j-=1
        
        return(maxTemp)
        