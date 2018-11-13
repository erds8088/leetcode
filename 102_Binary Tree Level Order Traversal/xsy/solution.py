# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        r = []
        def _levelOrder(root, level):
            if root is None:
                return
            if len(r) < level + 1:
                r.append([])
                r[level].append(root.val)
            _levelOrder(root.left, level + 1)
            _levelOrder(root.right, level + 1)
        _levelOrder(root, 0)
        return r
