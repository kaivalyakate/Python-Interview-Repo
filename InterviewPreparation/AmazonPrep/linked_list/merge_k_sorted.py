from typing import Optional
from node import ListNode
from heapq import heappop, heappush
from queue import PriorityQueue

def mergeKLists(lists: list[Optional[ListNode]]) -> Optional[ListNode]:
    amount = len(lists)
    interval = 1
    while interval < amount:
        for i in range(0, amount - interval, interval * 2):
            lists[i] = merge2Lists(lists[i], lists[i + interval])
        interval *= 2

    return lists[0] if amount > 0 else None

def merge2Lists(l1, l2):
    head = point = ListNode(0)
    while l1 and l2:
        if l1.val <= l2.val:
            point.next = l1
            l1 = l1.next
        else:
            point.next = l2
            l2 = l1
            l1 = point.next.next
        point = point.next

    if not l1:
        point.next=l2
    else:
        point.next=l1

    return head.next


if __name__ == "__main__":
    node = ListNode(1, ListNode(4, ListNode(5)))
    node1 = ListNode(1, ListNode(3, ListNode(4)))
    node2 = ListNode(2, ListNode(6))
    mergeKLists([node, node1, node2])