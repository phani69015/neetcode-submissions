# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #bruteforce 
        s1 = s2 = ""
        c1 = l1
        c2= l2
        while c1:
            s1+=str(c1.val)
            c1=c1.next
        while c2:
            s2+=str(c2.val)
            c2=c2.next
        r = int(s1[::-1])+int(s2[::-1]) 
        r = str(r)

        h = ListNode(0)
        dummy = h
        for i in r[::-1]:
            dummy.next = ListNode(int(i))
            dummy = dummy.next
        return h.next

        