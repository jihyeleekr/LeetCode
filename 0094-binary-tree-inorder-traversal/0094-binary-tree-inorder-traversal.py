# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        output = []
        self.traversal(root, output)
        return output

    def traversal(self, root, output):
        if root != None:
            self.traversal(root.left, output)
            output.append(root.val)
            self.traversal(root.right, output)
        else:
            return
        