class Solution:
    def temp(self,pos1,i):
        ans=0
        for j in pos1:
            ans+=abs(j-i)
        return(ans)

    def minOperations(self, boxes: str) -> List[int]:
        pos1=[]
        n=len(boxes)
        ans=[]

        for i in range(n):
            if(boxes[i]=='1'):
                pos1.append(i)

        for i in range(n):
            k=self.temp(pos1,i)
            ans.append(k)
        return(ans)
        