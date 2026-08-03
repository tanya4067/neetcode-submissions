class Solution:
    def temp(self,ans,result,mapTemp,digits,n,i):
        if(i>n):
            return
        if(len(ans)==n):
            x = "".join(ans)
            result.append(x)
            return
        for j in mapTemp[digits[i]]:
            ans.append(j)
            self.temp(ans,result,mapTemp,digits,n,i+1)
            ans.pop()

    def letterCombinations(self, digits: str) -> List[str]:
        mapTemp={"2":"abc","3":"def","4":"ghi",
            "5":"jkl","6":"mno","7":"pqrs",
            "8":"tuv","9":"wxyz"}
        
        ans=[]
        result=[]
        n=len(digits)
        if(n==0):
            return(result)
        self.temp(ans,result,mapTemp,digits,n,0)

        return(result)

        
        