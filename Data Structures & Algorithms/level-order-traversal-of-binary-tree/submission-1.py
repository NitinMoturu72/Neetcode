# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        stack = [[root, 0]]
        res = []
        while stack:
            pair = stack.pop()
            node = pair[0]
            level = pair[1]
            if node:
                stack.append([node.right, level+1])
                stack.append([node.left, level+1])
                if level == 0:
                    res.append([node.val])
                elif level <= len(res)-1:
                    res[level].append(node.val)
                else:
                    res.append([node.val])
        
        return res


            