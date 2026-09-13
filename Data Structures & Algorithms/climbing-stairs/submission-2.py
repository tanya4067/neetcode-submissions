class Solution:
    def climbStairsTemp(self,n:int,mapDict:dict)-> int:
        if(n==1):
            return(1)
        if(n==2):
            return(2)
        
        if(n in mapDict):
            return(mapDict[n])
        
        mapDict[n]=self.climbStairsTemp((n-1),mapDict)+self.climbStairsTemp((n-2),mapDict)

        return(mapDict[n])
    def climbStairs(self, n: int) -> int:

        mapDict = {}
        k = self.climbStairsTemp(n,mapDict)
        return(k)