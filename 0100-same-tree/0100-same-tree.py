# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        p_result = []
        q_result = []
        self.dfs(p, p_result)
        self.dfs(q, q_result)
        print(p_result, q_result)
        return p_result == q_result

    def dfs(self, root, result):
        if root == None:
            result.append("null")
        else:
            result.append(root.val)
            self.dfs(root.left, result)
            self.dfs(root.right, result)
        return result

