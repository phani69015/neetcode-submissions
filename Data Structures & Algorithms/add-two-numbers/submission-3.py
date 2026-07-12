# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #bruteforce 
        # s1 = s2 = ""
        # c1 = l1
        # c2= l2
        # while c1:
        #     s1+=str(c1.val)
        #     c1=c1.next
        # while c2:
        #     s2+=str(c2.val)
        #     c2=c2.next
        # r = int(s1[::-1])+int(s2[::-1]) 
        # r = str(r)

        # h = ListNode(0)
        # dummy = h
        # for i in r[::-1]:
        #     dummy.next = ListNode(int(i))
        #     dummy = dummy.next
        # return h.next

        #optimal 

        h1 = l1 
        h2 = l2
        c = 0
        new = ListNode(0) 
        ans = new 
        while h1 or h2:
            x = h1.val if h1 else 0
            y = h2.val if h2 else 0
            s = x+y+c
            ans.next = ListNode(s%10)
            c = s//10 
            h1 = h1.next if h1 else None
            h2 = h2.next if h2 else None
            ans = ans.next 
        if c > 0 :
            ans.next = ListNode(c) 
        return new.next


        