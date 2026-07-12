# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None:
            return l2 
        if l2 is None:
            return l1 
        dummy = ListNode(0)
        tail = dummy

        while l1 and l2 :
            if l1.val<=l2.val:
                tail.next = l1
                l1 = l1.next 
            elif l1.val>l2.val:
                tail.next = l2
                l2 = l2.next 
            tail = tail.next 
        tail.next = l1 if l1 else l2 

        return dummy.next
        