# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = [[root, float("-inf"), float("inf")]]
        while stack:
            pair = stack.pop()
            node = pair[0]
            left = pair[1]
            right = pair[2]

            if not node:
                continue
            
            if not (node.val > left and node.val < right):
                return False
            stack.append([node.left,left, node.val])
            stack.append([node.right, node.val, right])

        return True            
