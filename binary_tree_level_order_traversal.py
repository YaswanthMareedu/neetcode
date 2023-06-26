# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        if root==None:
            return []

        q = [root]
        while q:
            p=[]
            t=[]
            #print(q)
            for i in range(len(q)):
                tmp = q[i]
                if tmp.left!=None:
                    t.append(tmp.left)
                if tmp.right!=None:
                    t.append(tmp.right)
                p.append(tmp.val)
            q=t
            ans.append(p)
            
        return ans
            
            
