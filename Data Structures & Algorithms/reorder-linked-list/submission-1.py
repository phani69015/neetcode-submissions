# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #bruteforce
        # arr = []
        # curr = head
        # while curr:
        #     arr.append(curr)
        #     curr = curr.next 
        # i = 0 
        # j = len(arr)-1

        # while i<j:
        #     arr[i].next = arr[j]
        #     i+=1
        #     if i==j:
        #         break 
        #     arr[j].next = arr[i]
        #     j-=1 
        # arr[i].next = None 

        #optimal 
        #find the mid
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        #split into 2 
        secondHalf = slow.next 
        slow.next = None
        #reverse the 2nd half 
        prev = None 
        curr = secondHalf 
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr 
            curr = nxt 
        secondHalf = prev 

        #alternative merge of 2 lists 
        f = head
        while secondHalf:
            t1 = f.next
            t2 = secondHalf.next 

            f.next = secondHalf
            secondHalf.next = t1 

            f = t1 
            secondHalf = t2










    


        