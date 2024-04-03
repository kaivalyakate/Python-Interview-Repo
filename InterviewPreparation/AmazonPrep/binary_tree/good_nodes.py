from tree_node import TreeNode
import sys

def goodNodes(root: TreeNode) -> int:
    result = 0
    def helper(root: TreeNode, prev: int):
        if not root:
            return prev
        
        nonlocal result
        if root.val >= prev:
            result += 1
        
        if root.right:
            helper(root.right, max(root.val, prev))

        if root.left:
            helper(root.left, max(root.val, prev))
        
        helper(root, float("-inf"))
        return result


if __name__ == "__main__":
    node = TreeNode(3, left=TreeNode(1, left=TreeNode(3)), right=TreeNode(4, left=TreeNode(1), right=TreeNode(5)))
    goodNodes(node)