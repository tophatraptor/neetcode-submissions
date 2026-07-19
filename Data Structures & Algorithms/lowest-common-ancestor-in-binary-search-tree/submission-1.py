# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        cursor = root
        pnext = root
        qnext = root
        while True:
            if p.val == cursor.val:
                return cursor
            elif p.val < cursor.val:
                pnext = cursor.left
            else:
                pnext = cursor.right
            if q.val == cursor.val:
                return cursor
            elif q.val < cursor.val:
                qnext = cursor.left
            else:
                qnext = cursor.right
            if pnext != qnext:
                return cursor
            cursor = pnext

"""
So in effect, we recurse down until our cursors for p and q diverge, then return the current node
"""