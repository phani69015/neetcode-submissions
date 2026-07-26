from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = deque()
        ans = []
        q.append(root)
        while q:
            level = []
            for _ in range(len(q)):
                key = q.popleft()
                level.append(key.val)
                if key.left:
                    q.append(key.left)
                if key.right:
                    q.append(key.right)
            ans.append(level)
        return ans

        


        