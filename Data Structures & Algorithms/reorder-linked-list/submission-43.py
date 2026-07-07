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

        firstList = head

        while secondList:
            next_node = secondList.next
            secondList.next = prev
            prev = secondList
            secondList = next_node
        
        while firstList and prev:
            next_one = firstList.next
            next_two = prev.next

            firstList.next = prev
            prev.next = next_one

            firstList = next_one
            prev = next_two
        


        