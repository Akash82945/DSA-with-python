# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        # We start with a dummy node to simplify the 'next' pointer logic
        dummy = ListNode(0)
        curr = dummy
        carry = 0

        # Loop continues if there's a node left in l1, l2, or a remaining carry
        while l1 or l2 or carry:
            # Extract values, defaulting to 0 if we reached the end of a list
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # Core math: Sum the digits and handle the carry-over
            total = v1 + v2 + carry
            carry = total // 10
            val = total % 10

            # Create a new node with the single-digit result
            curr.next = ListNode(val)
            
            # Move our pointer forward
            curr = curr.next

            # Move the input list pointers forward if they exist
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        # Return the next node of dummy, which is the start of our actual result
        return dummy.next
        