# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.val)


class Solution:
    """
    对根节点左边的树采用前序遍历，右边采用类似前序的中右左遍历，依次比较值
    """
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



class Solution2:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not toot:
            return True
        return self.isSym(root.left, root.right)

    def isSym(self, l, r):
        if l and r and l.val == r.val:
            return self.isSym(l.left, r.right) and self.isSym(l.right, r.left)
        else:
            return l == r
