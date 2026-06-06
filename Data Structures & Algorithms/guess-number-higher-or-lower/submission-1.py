class Solution:
    def guessNumber(self, n: int) -> int:
        l=0
        r=n
        mid=(l+r)//2

        while(l<=r):
            mid=(l+r)//2
            x=guess(mid)

            if(x==0):
                return(mid)
            if(x==-1):
                r=mid
            if(x==1):
                l=mid+1
        
        return(mid)
        