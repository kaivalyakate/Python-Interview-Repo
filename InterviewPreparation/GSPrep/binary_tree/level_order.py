from typing import Optional, List
from tree_node import TreeNode
from collections import deque

def levelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    result = []
    if not root:
        return result
    
    queue = deque([root])
    level = 0
    while queue:
        result.append([])
        level_len = len(queue)

        for _ in range(level_len):
            node = queue.popleft()
            result[level].append(node.val)

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        level += 1

    return result
