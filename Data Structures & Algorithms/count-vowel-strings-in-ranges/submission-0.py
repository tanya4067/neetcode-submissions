class Solution:
    def tempVowel(self,words):
        n=len(words)
        a=words[0]
        b=words[n-1]
        if((a=='a' or a=='i' or a=='e' or a=='o' or a=='u')and(b=='a' or b=='i' or b=='e' or b=='o' or b=='u')):
            return(True)
        return(False)
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        ans=[]
        for i in queries:
            left=i[0]
            right=i[1]
            c=0
            for j in range(left,right+1):
                if(self.tempVowel(words[j])):
                    c+=1
            ans.append(c)
        return(ans)
        