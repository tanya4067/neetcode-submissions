class Solution:

    def encode(self, strs: List[str]) -> str:
        s=""
        for i in strs:
            s+=i
            s+="qwerty"
        return(s)

    def decode(self, s: str) -> List[str]:
        # print(s)
        ans=s.split("qwerty")
        temp=[]
        for i in ans:
            temp.append(i)

        return(temp[:len(temp)-1])

