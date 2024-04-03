from tree_node import TreeNode
from collections import deque

def right_view(root: TreeNode):
    q = deque([root])
    ans = [root.val]
    while q:
        level_nodes = []
        while q:
            node = q.popleft()
            if node.left:
                level_nodes.append(node.left)
            if node.right:
                level_nodes.append(node.right)
        if level_nodes:
            ans.append(level_nodes[-1].val)
        q.extend(level_nodes)
    return ans


if __name__ == "__main__":
    root = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3, TreeNode(5, None, TreeNode(6)), TreeNode(4)))
    right_view(root)