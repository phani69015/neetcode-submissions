# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #bruteforce 
        d = {}
        curr = head
        while curr:
            if curr in d:
                return True 
            d[curr] = curr.val 
            curr = curr.next 
        return False
        #naive approach
        # slow = fast = head
        # while fast and fast.next:
        #     slow = slow.next
        #     fast = fast.next.next
        #     if slow == fast :
        #         return True
        # return False
    

        