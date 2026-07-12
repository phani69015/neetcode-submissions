# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:   

    def mergetwolists(self, l1:Optional[ListNode], l2:Optional[ListNode]):
        if l1 is None:
            return l2 
        if l2 is None:
            return l1 

        dummy = ListNode(-1)
        ans = dummy 

        while l1 and l2:
            if l1.val<=l2.val:
                ans.next = ListNode(l1.val)
                l1 = l1.next 
            elif l1.val>l2.val:
                ans.next = ListNode(l2.val)
                l2=l2.next  
            ans = ans.next
        ans.next = l1 if l1 else l2
        return dummy.next


    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or not lists[0]:
            return None 
        
        #bruteforce 
        # temp = []
        # for i in lists:
        #     curr = i 
        #     while curr:
        #         temp.append(curr.val)
        #         curr = curr.next 
        # temp.sort()
        # ans = ListNode(0)
        # dummy = ans 
        # for i in temp:
        #     node = ListNode(i)
        #     dummy.next = node
        #     dummy = dummy.next 
        # return ans.next

        #optimal 1 using merge 2 lists function 

        # n = len(lists)-1
        # while n > 0:
        #     lists[0] = self.mergetwolists(lists[0],lists[n])
        #     n-=1 
        # return lists[0]

        #optimal 2 using min heap 
        dummy = ListNode(-1)
        ans = dummy 
        temp_heap = []
        ctr = count()
        for ll in lists:
            if ll!=None:
                heapq.heappush(temp_heap,(ll.val,next(ctr),ll))
        while temp_heap:
            _,_,node = heapq.heappop(temp_heap)
            if node.next is not None:
                heapq.heappush(temp_heap,(node.next.val,next(ctr),node.next))
            ans.next = node
            ans = ans.next
        return dummy.next






        
         






        