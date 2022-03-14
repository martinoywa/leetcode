# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root:
            # final queue
            f = [[root.val]]
            # get children
            c_current = []
            c_nodes = []
            if root.left:
                c_current.append(root.left.val)
                c_nodes.append(root.left)
                # c_current_nodes.append(t[0].left)
            if root.right:
                c_current.append(root.right.val)
                c_nodes.append(root.right)
            # store in final if children exist
            if c_current:
                f.append(c_current)

            # get children of children iteratively
            while c_nodes:
                c_c_current, c_c_nodes = [], [] # children of children
                for node in c_nodes:
                    if node.left:
                        c_c_current.append(node.left.val)
                        c_c_nodes.append(node.left)
                    if node.right:
                        c_c_current.append(node.right.val)
                        c_c_nodes.append(node.right)

                if c_c_current:
                    f.append(c_c_current)

                # set the childre of children nodes to be children nodes
                c_nodes = c_c_nodes

            return f
        return []
                
