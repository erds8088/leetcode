# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root is None:
            return False
        if not root.left and not root.right and root.val == sum:
            return True
        sum = sum - root.val
        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)


if __name__ == '__main__':
    root = TreeNode(5, left=TreeNode(4, left=TreeNode(11)), right=TreeNode(8, left=TreeNode(13), right=TreeNode(4)))
    s = Solution()
    print(s.hasPathSum(root, 20))
