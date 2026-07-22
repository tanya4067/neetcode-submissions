# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def temp(self,root,ans):
        if(root is None):
            return
        
        self.temp(root.left,ans)
        ans.append(root.val)
        self.temp(root.right,ans)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans=[]
        self.temp(root,ans)
        n=len(ans)
        return(ans[k-1])