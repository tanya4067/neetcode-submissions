class Solution:
    def temp(self,s,i,j):
        while(i<j):
            if(s[i]!=s[j]):
                return(False)
            i+=1
            j-=1
        return(True)

    def validPalindrome(self, s: str) -> bool:
        n=len(s)
        i=0
        j=n-1
        
        while(i<j):
            if(s[i]!=s[j]):
                return(self.temp(s,i+1,j) or self.temp(s,i,j-1))
            
            i+=1
            j-=1
        return(True)
        