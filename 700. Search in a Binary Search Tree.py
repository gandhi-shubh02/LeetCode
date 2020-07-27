# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root is None:
            return []
        else:
            nodes=[root]
            while nodes:
                temp=[]
                for node in nodes:
                    if node.val==val:
                        return node
                    if node.right:
                        temp.append(node.right)
                    if node.left:
                        temp.append(node.left)
                nodes=temp
                
