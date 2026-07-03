# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        dummy = ListNode(0,head)
        fast = dummy
        slow = dummy

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        list2 = slow.next
        slow.next = None

        prev = None
        cur = list2
        while cur:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node
        
        list1 = head
        tmp_head = list2
        while list1 and prev:
            next_one = list1.next
            next_two = prev.next

            list1.next = prev
            prev.next = next_one

            list1 = next_one
            prev = next_two

        
            

        

        