class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1=""
        s2=""
        for i in s:
            if(i.isalnum()):
                s1=i+s1
                s2=s2+i

        
        s2=s2.lower()
        s1=s1.lower()

        print(s2)
        print(s1)

        if(s2==s1):
            return(True)
        return(False)

        