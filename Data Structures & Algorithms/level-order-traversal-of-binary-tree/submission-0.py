class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue=[]
        queue.append(root)

        result=[]

        while(len(queue)!=0):
            ans=[]
            for i in range(len(queue)):
                temp=queue.pop(0)
                if(temp is not None):
                    ans.append(temp.val)
                    if(temp.left):
                        queue.append(temp.left)
                    if(temp.right):
                        queue.append(temp.right)
            result.append(ans)
        
        if(len(result[0]) == 0):
            return []
        # print(len(result[0]))
        return(result)
        