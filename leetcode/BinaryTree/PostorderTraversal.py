#106. Construct Binary Tree from Inorder and Postorder Traversal


class Solution:
    def buildTree(self, inorder, postorder):
        index_map = {value: index for index, value in enumerate(inorder)}
        postorder_index = len(postorder) - 1

        def build(left, right):
            nonlocal postorder_index

            if left > right:
                return None

            root_val = postorder[postorder_index]
            postorder_index -= 1

            root = TreeNode(root_val)
            root_index = index_map[root_val]

            root.right = build(root_index + 1, right)
            root.left = build(left, root_index - 1)

            return root

        return build(0, len(inorder) - 1)