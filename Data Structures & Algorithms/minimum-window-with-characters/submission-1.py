class Solution:
    def remove(self,test,ch):
        x=test[ch]-1
        if(x==0):
            test.pop(ch)
        else:
            test[ch]=x
        
        return(test)
    def minWindow(self, s: str, t: str) -> str:
        
        tmap={}
        for i in range(0,len(t)):
            ch=t[i]
            if(t[i] in tmap):
                tmap[ch]+=1
            else:
                tmap[ch]=1
        
        n=len(s)
        i=0
        j=0
        minans=1000000
        result=""
    
        while(i<n):
            ch=s[i]
            ans=[]
            if(ch in tmap):
                j=i
                test=tmap.copy()
                while(len(test)!=0 and j<n):
                    ch1=s[j]
                    if(ch1 in test):
                        test=self.remove(test,ch1)
                    
                    ans.append(ch1)
                    j+=1
                
                
                if(len(ans)<minans and len(test)==0):
                    minans=len(ans)
                    result="".join(ans)
               
                
            i+=1
        return(result)
        
        