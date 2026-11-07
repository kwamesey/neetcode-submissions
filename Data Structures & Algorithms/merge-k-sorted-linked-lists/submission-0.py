# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if lists == []:
            return 

        dummy = ListNode(-1)
        curr = dummy
        
        min_heap = []

        for i,head in enumerate(lists):
            if head is not None:
                heapq.heappush(min_heap,(head.val,i,head))

        while min_heap:
            val, i ,node = heapq.heappop(min_heap)
            curr.next = node
            curr = curr.next
            if node.next is not None:
                heapq.heappush(min_heap, (node.next.val,i,node.next))

                
        
        return dummy.next


        

        