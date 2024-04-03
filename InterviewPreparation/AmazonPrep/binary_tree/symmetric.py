from tree_node import TreeNode
from collections import deque

def symmetric(root: TreeNode):
    
    return True


if __name__ == "__main__":
    root = TreeNode(1, TreeNode(2, None, TreeNode(3)), TreeNode(2, None, TreeNode(3)))
    print(symmetric(root))