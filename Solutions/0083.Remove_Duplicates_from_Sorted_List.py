"""
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

Example 1:


Input: head = [1,1,2]
Output: [1,2]
Example 2:


Input: head = [1,1,2,3,3]
Output: [1,2,3]

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or not head.next:
            return head
        
        curr1, curr2 = head, head.next
        while curr2 != None:
            if curr1.val == curr2.val:
                curr2 = curr2.next
            else:
                curr1.next = curr2
                curr1 = curr1.next
                curr2 = curr2.next
        curr1.next = None
        return head
            


