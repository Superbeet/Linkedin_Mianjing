# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        self.add_leaves(root, result)
        return result
    
    def add_leaves(self, root, res):
        if root is None:
            return 0
        
        left = self.add_leaves(root.left, res)
        right = self.add_leaves(root.right, res)
        
        depth = max(left, right) + 1
        if depth > len(res):
            res.append([])
        res[depth-1].append(root.val)
        
        return depth
        
        
        