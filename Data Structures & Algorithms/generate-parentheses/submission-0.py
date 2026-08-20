class Solution:
    def isValid(self,ans):
        stack=[]

        for i in ans:
            if(i=='('):
                stack.append(i)
            else:
                n=len(stack)
                if(n==0):
                    return(False)
                stack.pop()
        if(len(stack)>0):
            return(False)
        return(True)

    def temp(self,ans,result,n,i):
        if(i>n):
            return
        
        if(len(ans)==n):
            if(self.isValid(ans)):
                print(ans)
                result.append(''.join(ans))
            return
        
        #consider the )
        ans.append('(')
        self.temp(ans,result,n,i+1)
        ans.pop()
        #consider the (
        ans.append(')')
        self.temp(ans,result,n,i+1)
        ans.pop()
        

    def generateParenthesis(self, n: int) -> List[str]:
        ans=[]
        result=[]
        n*=2
        self.temp(ans,result,n,0)
        print(result)
        return(result)
        