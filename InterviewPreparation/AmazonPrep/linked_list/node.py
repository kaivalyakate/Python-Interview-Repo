from __future__ import annotations
from typing import Optional


class ListNode:

    def __init__(self, val: int = 0, next: Optional[ListNode] = None) -> None:
        self.val = val
        self.next = next