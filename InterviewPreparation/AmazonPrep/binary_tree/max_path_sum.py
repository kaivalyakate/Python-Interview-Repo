from tree_node import TreeNode

def binary_tree_max_path_sum(root: TreeNode):
    max_path_sum = float("-inf")
    def max_sum(node: TreeNode):
        nonlocal max_path_sum
        if not node:
            return None
        
        max_left_path = max(max_sum(node.left), 0)
        max_right_path = max(max_sum(node.right, 0))

        max_path_sum = max(max_path_sum, node.val + max_left_path + max_right_path)

        return node.val + max(max_left_path, max_right_path)

    return max_sum(root)

if __name__ == "__main__":
    root = TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    binary_tree_max_path_sum(root=root)