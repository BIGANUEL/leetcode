# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        vals = []
        def inorder(node):
            if not node:
                return None
            inorder(node.left)
            vals.append(node.val)
            inorder(node.right)
            return node
        inorder(root)

        def build(l,r):
            if l > r:
                return None
            mid = (l+r)//2
            node = TreeNode(vals[mid])
            node.left = build(l,mid-1)
            node.right = build(mid + 1,r)
            return node
        return build(0,len(vals)-1)