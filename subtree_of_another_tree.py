# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorder(self,root):
        if root==None:
            return [None]
        return self.postorder(root.left)+self.postorder(root.right)+[root.val]
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root==None:
            return False
        if self.postorder(root)==self.postorder(subRoot):
            return True
        return self.isSubtree(root.left,subRoot) | self.isSubtree(root.right,subRoot)
        
