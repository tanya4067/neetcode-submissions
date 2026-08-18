class Solution:
    def scoreOfString(self, s: str) -> int:
        n=len(s)
        ans=0
        for i in range(1,n):
            a=ord(s[i])
            b=ord(s[i-1])
            ans+=abs(a-b)

        return(ans)

        