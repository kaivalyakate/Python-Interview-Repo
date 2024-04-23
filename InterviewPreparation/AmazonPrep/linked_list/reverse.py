from __future__ import annotations
from typing import Optional

class ListNode:

    def __init__(self, val: int = 0, next: Optional[ListNode] = None) -> None:
        self.val = val
        self.next = next


def reverseLinkedList(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head or (not head.next):
        return head
    
    ans = None
    def helper(current: ListNode):
        nonlocal ans
        if current.next == None:
            ans = current
            return current
        prev = helper(current.next)
        prev.next = current
        current.next = None
        return current
    
    helper(head)
    return ans


if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    reverseLinkedList(head=head)