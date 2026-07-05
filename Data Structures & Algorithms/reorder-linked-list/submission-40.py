# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        cur = head
        dummy = ListNode(0,head)

        fast = dummy
        slow = dummy

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        secondList = slow.next
        slow.next = None

        prev = None
        while secondList:
            next_node = secondList.next
            secondList.next = prev
            prev = secondList
            secondList = next_node

        firstList = head
        secondList = prev

        while firstList and secondList:
            next_one = firstList.next
            next_two = secondList.next

            firstList.next = secondList
            secondList.next = next_one

            firstList = next_one
            secondList = next_two 

