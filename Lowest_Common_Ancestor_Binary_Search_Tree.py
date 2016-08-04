# Definition for a binary tree node.
# class TreeNode(object):
#	 def __init__(self, x):
#		 self.val = x
#		 self.left = None
#		 self.right = None

# BST
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        
        if root==None:
            return None
        
        if p.val>q.val:
            return self.lowestCommonAncestor(root, q, p)
        
        elif p.val<root.val and q.val<root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        
        elif p.val>root.val and q.val>root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        
        else:
            return root

# BT
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        
        if root is None or root == p or root == q:
            return root 
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        if left is not None and right is not None:
            return root
        
        if left is not None:
            return left
        
        if right is not None:
            return right
        
        return None