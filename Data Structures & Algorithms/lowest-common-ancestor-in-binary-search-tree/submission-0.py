# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # We traverse from the root until we reach a point where the next child for p and q are not the same
        pnext = root
        qnext = root
        cur_node = root
        while pnext == qnext:
            cur_node = pnext
            if p.val == cur_node.val:
                return cur_node
            if q.val == cur_node.val:
                return cur_node
            if p.val < cur_node.val:
                pnext = cur_node.left
            else:
                pnext = cur_node.right
            if q.val < cur_node.val:
                qnext = cur_node.left
            else:
                qnext = cur_node.right
        return cur_node