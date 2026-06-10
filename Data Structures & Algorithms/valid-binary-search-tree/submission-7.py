# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def check(self,root,mini,maxi):
        if(root is None):
            return(True)
        
        if(root.val<=mini or root.val>=maxi):
            return(False)
        
        left=self.check(root.left,mini,root.val)
        right=self.check(root.right,root.val,maxi)

        return(left and right)
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        mini=-1000000
        maxi=1000000

        k = self.check(root,mini,maxi)
        return(k)

        