# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.val)

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        for i, j in zip(self.preOrder(root.left), self.mirrorPreOrder(root.right)):
            if i != j:
                return False
        return True

    def preOrder(self ,root):
        """中左右遍历"""
        if not root:
            yield None
        else:
            yield root.val
            yield from self.preOrder(root.left)
            yield from self.preOrder(root.right)

    def mirrorPreOrder(self, root):
        """中右左遍历"""
        if not root:
            yield None
        else:
            yield root.val
            yield from self.mirrorPreOrder(root.right)
            yield from self.mirrorPreOrder(root.left)
