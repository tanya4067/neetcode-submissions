class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue=[]
        queue.append(root)
        result=[]
        while(len(queue)!=0):
            ans=[]
            for i in range(0,len(queue)):

                temp=queue.pop(0)
                if(temp is not None):
                    ans.append(temp.val)
                    if(temp.left):
                        queue.append(temp.left)
                    
                    if(temp.right):
                        queue.append(temp.right)
            n=len(ans)
            if(n>=1):
                result.append(ans[n-1])
        
        return result
        

        
        