# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        l = 0
        curr = head 
        while curr:
            curr = curr.next 
            l+=1
        r = l - n 
        curr = head 
        prev = dummy
        while r>0:
            prev = curr
            curr = curr.next 
            r-=1
        prev.next = curr.next 
        return dummy.next 

        