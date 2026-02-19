# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: ListNode
        :type list2: ListNode
        :rtype: ListNode
        """
        # 1. Create a dummy node to act as the start
        dummy = ListNode(0)
        cur = dummy
        
        # 2. While both lists have nodes remaining
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            
            # Move our builder pointer forward
            cur = cur.next
            
        # 3. If one list is finished, attach the remainder of the other list
        cur.next = list1 if list1 else list2
        
        # 4. Return the head of the new list (skipping the dummy)
        return dummy.next