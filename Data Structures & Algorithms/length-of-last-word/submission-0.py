class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        c=0
        
        s1=s.strip()
        n=len(s1)

        for i in range(n):
            if(s1[n-i-1]==' '):
                return(c)
            c+=1
        return(c)
        