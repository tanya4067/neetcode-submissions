# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self,root,p1,q1):
        value=root.val
        p=p1.val
        q=q1.val
        if(p>value and q>value):
            return(self.dfs(root.right,p1,q1))
        
        if(p<value and q<value):
            return(self.dfs(root.left,p1,q1))
        
        return(root)
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        k=self.dfs(root,p,q)
        
        return(k)
        