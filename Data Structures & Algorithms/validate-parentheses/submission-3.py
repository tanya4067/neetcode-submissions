class Solution:
    def isValid(self, s: str) -> bool:
        ans=[]
        for i in s:
            if(i=='(' or i=='{' or i=='['):
                ans.append(i)
            else:
                if(len(ans)==0):
                    return(False)
                x=ans.pop()
                if(i==')' and x!='('):
                    return(False)
                if(i=='}' and x!='{'):
                    return(False)
                if(i==']' and x!='['):
                    return(False)
        if(len(ans)>0):
            return(False)
        return(True)
                

        