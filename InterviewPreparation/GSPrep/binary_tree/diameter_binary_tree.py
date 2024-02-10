from tree_node import TreeNode
from typing import Optional

def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    res = 0

    def dfs(root: Optional[TreeNode]):
        if not root:
            return 0
        
        nonlocal res
        left = dfs(root.left)
        right = dfs(root.right)
        res = max(res, 1 + left + right)

        return 1 + max(left, right)
    
    dfs(root=root)

    return res


if __name__ == "__main__":
    pass