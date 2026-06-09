# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxRight(self,root):
        while(root.right is not None):
            root=root.right
        return(root)

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        if(root is None):
            return
        
        if(root.val==key):
            # 0 child
            if(root.left is None and root.right is None):
                root=None
                return(root)
            # 1 child
            if(root.left is not None and root.right is None):
                root=root.left
                return(root)
            if(root.left is None and root.right is not None):
                root=root.right
                return(root)
            # 2 child
            if(root.left is not None and root.right is not None):
                k=self.maxRight(root.left)
                root.val=k.val
                root.left=self.deleteNode(root.left,k.val)
                return(root)

        elif(root.val>key):
            root.left=self.deleteNode(root.left,key)
        elif(root.val<key):
            root.right=self.deleteNode(root.right,key)
        
        return(root)


        