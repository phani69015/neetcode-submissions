# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or not lists[0]:
            return None 
        
        #bruteforce 
        temp = []
        for i in lists:
            curr = i 
            while curr:
                temp.append(curr.val)
                curr = curr.next 
        temp.sort()
        ans = ListNode(0)
        dummy = ans 
        for i in temp:
            node = ListNode(i)
            dummy.next = node
            dummy = dummy.next 
        return ans.next


        