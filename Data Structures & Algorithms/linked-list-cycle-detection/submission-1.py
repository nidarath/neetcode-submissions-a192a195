# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hashset = set()
        while head: 
            # check if in hashset, if yes: TRUE
            if(head in hashset):
                return True
            else:
            # else add to hashset, move pointer
                hashset.add(head)
                head = head.next
        # if reaches null: FALSE
        return False