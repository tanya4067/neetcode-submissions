class Solution:
    def left(self,s):
        left0=0
        for i in s:
            if(i=='0'):
                left0+=1
        return(left0)
    
    def right(self,s):
        right1=0
        for i in s:
            if(i=='1'):
                right1+=1
        return(right1)

    def maxScore(self, s: str) -> int:
        n=len(s)
        maxAns=0

        for i in range(1,n):
            l=self.left(s[:i])
            r=self.right(s[i:])

            maxAns=max(maxAns,(l+r))
        return(maxAns)

        