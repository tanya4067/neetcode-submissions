class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n=len(s)
        a=[]

        for i in range(n):
            a.append(s[n-i-1])
        
        for i in range(n):
            s[i]=a[i]
        