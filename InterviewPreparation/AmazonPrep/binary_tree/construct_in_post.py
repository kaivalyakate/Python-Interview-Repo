from tree_node import TreeNode

def buildTree(inorder: list[int], postorder: list[int]):
    def array_to_tree(left, right):
        if left > right: return None

        nonlocal postorder_idx
        root_v = postorder[postorder_idx]
        root = TreeNode(root_v)

        postorder_idx -= 1
        root.right = array_to_tree(inorder_idx[root_v]+1, right)
        root.left = array_to_tree(left, inorder_idx[root_v] - 1)

        return root

    postorder_idx = len(inorder) - 1
    inorder_idx = {}
    for idx, v in enumerate(inorder):
        inorder_idx[v] = idx
    return array_to_tree(0, len(inorder) - 1)


if __name__ == "__main__":
    buildTree([9,3,15,20,7],[9,15,7,20,3])