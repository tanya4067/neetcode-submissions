class Solution:
    def calPoints(self, operations: List[str]) -> int:
        ans=[]
        for i in operations:
            if(i=='C' and ans!=None):
                ans.pop()
            elif(i=='D'):
                x=ans[-1]
                ans.append(2*x)
            elif(i=='+'):
                n=len(ans)
                x=sum(ans[n-2:])
                ans.append(x)
            else:
                ans.append(int(i))
        
        return(sum(ans))
        