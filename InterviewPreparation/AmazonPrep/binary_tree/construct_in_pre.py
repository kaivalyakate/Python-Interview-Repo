from tree_node import TreeNode

def buildTree(preorder: list[int], inorder: list[int]):
    def array_to_tree(left, right):
        if left > right: return None

        nonlocal preorder_index

        root_v = preorder[preorder_index]
        root = inorder_idx[root_v]

        preorder_index += 1

        root.left = array_to_tree(left, inorder_idx[root_v] - 1)
        root.right = array_to_tree(inorder_idx[root_v]+1, right)

        return root

    preorder_index = 0

    inorder_idx = {}
    for idx, v in enumerate(inorder):
        inorder_idx[v] = idx

    return buildTree(0, len(preorder) - 1)

if __name__ == "__main__":
    buildTree([3,9,20,15,7],[9,3,15,20,7])