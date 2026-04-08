# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        #while not null
        while fast and fast.next:
        #slow moves by one
            slow = slow.next
        #fast moves by two
            fast = fast.next.next
            # if cycle slow & fast meets return true
            if slow == fast:
                return True
        # if fast points to null then return false
        return False
