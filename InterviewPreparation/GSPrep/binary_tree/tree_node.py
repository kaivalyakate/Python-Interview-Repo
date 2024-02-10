from __future__ import annotations
from typing import *

class TreeNode:

    def __init__(self, val: Union[int, str], left: TreeNode = None, right: TreeNode = None) -> None:
        self.val = val
        self.right = right
        self.left = left