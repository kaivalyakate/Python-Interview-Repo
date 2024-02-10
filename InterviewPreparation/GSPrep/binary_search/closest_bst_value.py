from typing import *
import math
import sys
sys.path.insert(0, '/Users/kkate/PycharmProjects/pythonProject/InterviewPreparation/GSPrep/binary_tree')

import binary_tree
from binary_tree.tree_node import TreeNode

def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        min_diff = math.inf
        ans = -1  
        def find_closest(node: TreeNode):
            if not node:
                return None
            
            nonlocal min_diff
            diff = abs(node.val - target)
            if target > node.val:
                find_closest(node.right)

            if target < node.val and diff < min_diff:
                min_diff = diff
                ans = node.val
                find_closest(node.left)
        find_closest(root)
        return ans


if __name__ == "__main__":
    root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(5))
    closestValue(root)