class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        temp=[]
        n=len(s)
        i,j=0,0
        max_value=0
        while(j<n):
            while(s[j] in temp):
                temp.pop(0)
                i+=1
            
            temp.append(s[j])
            max_value=max(max_value,len(temp))
            j+=1
        return(max_value)

        