# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        headdummy = tail = ListNode()
        while list1 and list2:
            # if less or equal to
            if list1.val <= list2.val:
                #add to our list
                tail.next = list1
                # move to next node in list1
                list1 = list1.next
            else: # if greater than
                # add list2 to our list 
                tail.next = list2
                #move list to next node
                list2 = list2.next
            tail = tail.next
        #add the rest if any left
        if list1:
            tail.next = list1
        if list2:
            tail.next = list2
        
        # head is dummy node that points to head 
        return headdummy.next