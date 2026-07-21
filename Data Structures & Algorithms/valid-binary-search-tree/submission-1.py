# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isHelperBST(root,minval,maxval):
            if root == None:
                return True
            if root.val <= minval or root.val >= maxval:
                return False
            return isHelperBST(root.left,minval,root.val) and isHelperBST(root.right,root.val,maxval)
        return isHelperBST(root,float('-inf'),float('inf'))


        