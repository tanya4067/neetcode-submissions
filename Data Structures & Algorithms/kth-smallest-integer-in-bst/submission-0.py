# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorderTemp(self,root,ans):
        if(root is None):
            return
        
        self.inorderTemp(root.left,ans)
        ans.append(root.val)
        self.inorderTemp(root.right,ans)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        ans=[]
        self.inorderTemp(root,ans)
        print(ans)
        return(ans[k-1])
        