from tree_node import TreeNode
def kthsmallest(root: TreeNode, k: int):
    arr = []
    def dfs(node):
        if not node:
            return None
        dfs(node.left)
        arr.append(node.val)
        dfs(node.right)

    dfs(root)
    return arr[k-1] if k < len(arr) and k >= 0 else None


if __name__ == "__main__":
    root = TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4))
    kthsmallest(root, 1)