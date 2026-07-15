# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rotateArraybyKtimes(self, arr:Optional[List],k:int):
        n = len(arr)
        for start in range(0, n, k):
            if start + k > n:   
                break
            left, right = start, start + k - 1
            while left < right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1
        
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # bruteforce using an array

        # arr = []
        # curr = head
        # while curr:
        #     arr.append(curr.val)
        #     curr= curr.next
        # self.rotateArraybyKtimes(arr,k)

        dummy = ListNode(-1,head)
        group_prev = dummy

        # for i in arr:
        #     ans.next = ListNode(i)
        #     ans = ans.next
        # return dummy.next

        #optimal using 2 pointers
        while True:
            kth = group_prev
            for _ in range(k):
                kth = kth.next
                if kth is None:
                    return dummy.next

            group_next = kth.next

            prev = group_next
            curr = group_prev.next
            while curr != group_next:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt

            tail = group_prev.next
            group_prev.next = kth
            group_prev = tail

            
                 
                







        




        