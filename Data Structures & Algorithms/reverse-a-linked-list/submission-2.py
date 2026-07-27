# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #pointers
        prev, curr = None, head

        #while there is a list
        while curr:
            #reverse
            temp = curr.next # hold the node next to it temporarily
            curr.next = prev # turn curr next pointer the other way
            #move
            prev = curr #move prev to the current node
            curr = temp # move current to the next node
        return prev # return the list, curr will be at null so prev holds the new head