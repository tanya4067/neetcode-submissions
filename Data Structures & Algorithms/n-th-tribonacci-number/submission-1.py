class Solution:
    def temp(self,n,map_dict):
        if(n in map_dict):
            return(map_dict[n])
        if(n<=0):
            return(0)
        
        if(n==1 or n==2):
            return(1)
        
        map_dict[n]=(self.temp(n-1,map_dict)+self.temp(n-2,map_dict)+self.temp(n-3,map_dict))
        return(map_dict[n])
    def tribonacci(self, n: int) -> int:
        #recursion
        #memoization
        #top down approach
        map_dict={}
        k=self.temp(n,map_dict)
        return(k)
        