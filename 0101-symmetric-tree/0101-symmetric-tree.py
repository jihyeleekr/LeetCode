# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        right_result = []
        left_result = []
        self.right_subtree(root.right, right_result)
        self.left_subtree(root.left, left_result)
        print(right_result, left_result)
        return right_result == left_result
        
    def right_subtree(self, root, result):
        if root == None:
            result.append("null")
        else:
            result.append(root.val)
            self.right_subtree(root.right, result)
            self.left_subtree(root.left, result)
        return result
    def left_subtree(self, root, result):
        if root == None:
            result.append("null")
        else:
            result.append(root.val)
            self.left_subtree(root.left, result)
            self.right_subtree(root.right, result)
        return result
        