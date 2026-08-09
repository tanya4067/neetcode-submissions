class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ns=len(s)
        nt=len(t)

        if(ns==0):
            return(True)
        if(nt<ns ):
            return(False)
        

        i,j=0,0

        while(i<ns and j<nt):
            x=s[i]
            flag=0
            while(j<nt):
                if(t[j]!=x):
                    j+=1
                else:
                    break
            print("i: ",i,"j: ",j)
            j+=1
            i+=1

        
        if(i!=ns):
            return(False)
        
        return(True)
        