"""
 You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

Example 1:


Input: l1 = [7,2,4,3], l2 = [5,6,4]
Output: [7,8,0,7]
Example 2:

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [8,0,7]
Example 3:

Input: l1 = [0], l2 = [0]
Output: [0]  
"""
  
  # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#reverse the list, then do exactly the same as LC2
#then reverse again

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = 0
        while l1:
            num1 = num1 * 10 + l1.val
            l1 = l1.next
        
        num2 = 0
        while l2:
            num2 = num2 * 10 + l2.val
            l2 = l2.next
            
        nums = str(num1 + num2)
        
        head = ListNode(int(nums[0]))
        dummy = ListNode(0, head)
        
        for i in range(1, len(nums)):
            head.next = ListNode(int(nums[i]))
            head = head.next
        return dummy.next
