import math
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        h=head
        while head.next:
            head.next=ListNode(math.gcd(head.val,head.next.val),head.next)
            head=head.next.next
        return h
        