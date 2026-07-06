# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        dummy = ListNode(0,head)
        slow = dummy
        fast = dummy

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        secondList = slow.next
        slow.next = None
        prev = None
        cur = secondList

        while cur:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node
        
        firstList = head
        secondList = prev
        while firstList and secondList:
            next_one = firstList.next
            next_two = secondList.next

            firstList.next = secondList
            secondList.next = next_one

            firstList = next_one
            secondList = next_two
        