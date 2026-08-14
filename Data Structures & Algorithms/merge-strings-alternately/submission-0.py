class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans=""
        i,j=0,0
        n1=len(word1)
        n2=len(word2)

        while(i<n1 and j<n2):
            ans+=word1[i]
            ans+=word2[j]

            i+=1
            j+=1
        
        if(i==n1):
            ans+=word2[j:]
        elif(j==n2):
            ans+=word1[i:]
        
        return(ans)
        