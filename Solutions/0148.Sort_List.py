"""
Given the head of a linked list, return the list after sorting it in ascending order.

 

Example 1:


Input: head = [4,2,1,3]
Output: [1,2,3,4]
Example 2:


Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]
Example 3:

Input: head = []
Output: []
 

Constraints:

The number of nodes in the list is in the range [0, 5 * 104].
-105 <= Node.val <= 105
 

Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        #step1: find mid value
        dummy = ListNode(head)
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        rightHead = slow.next    #易错点，slow偏左，所以rightHead = slow.next
        slow.next = None
        
        #step2: divide
        l1 = self.sortList(head)
        l2 = self.sortList(rightHead)
        
        #step3: conquer
        new_dummy = curr = ListNode()
        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = l1
                curr = curr.next
                l1 = l1.next
            else:
                curr.next = l2
                curr = curr.next
                l2 = l2.next
        if l1:
            curr.next = l1
        if l2:
            curr.next = l2
            
        return new_dummy.next


//version 2 同version 1 就是分成了2个函数       
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# O(NlogN), O(1)"""

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        # step 1: find the mid of the list
        slow, fast = head, head.next    #注意这里slow, fast，不同于找环的快慢指针, 一定要记住不能写成slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # step 2: cut the list into two equal parts
        rightHead = slow.next
        slow.next = None
        
        # step 3: devide into two parts and recrussviely sort left and right
        sortedLeftHead = self.sortList(head)
        sortedRightHead = self.sortList(rightHead)
        return self.merge(sortedLeftHead, sortedRightHead)
        
    def merge(self, sortedLeftHead: [ListNode], sortedRightHead: [ListNode]) -> Optional[ListNode]:
        # step 4: merge the left and right part, by comparing
        dummyNode = ListNode(0)
        curr = dummyNode
        currLeft, currRight = sortedLeftHead, sortedRightHead
        while currLeft and currRight:
            if currLeft.val < currRight.val:
                curr.next = currLeft
                curr = curr.next
                currLeft = currLeft.next
            else:
                curr.next = currRight
                curr = curr.next
                currRight = currRight.next
                
        if currLeft:
            curr.next = currLeft
        
        if currRight:
            curr.next = currRight
          
        return dummyNode.next     
        
