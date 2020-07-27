# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        else:
            count=0
            nodes=[root]
            while nodes:
                temp=[]
                for node in nodes:
                    if node.left:
                        temp.append(node.left)
                    if node.right:
                        temp.append(node.right)
                count+=1
                nodes=temp
            return count
                    
