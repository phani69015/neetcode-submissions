# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        curr = head
        while curr:
            arr.append(curr.val)
            curr=curr.next 
        arr = arr[::-1]
        curr = head
        for i in range (len(arr)):
            curr.val = arr[i]
            curr=curr.next 
        return head
        