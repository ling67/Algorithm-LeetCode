"""
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

 

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []
 

Constraints:

k == lists.length
0 <= k <= 104
0 <= lists[i].length <= 500
-104 <= lists[i][j] <= 104
lists[i] is sorted in ascending order.
The sum of lists[i].length will not exceed 104.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
很多种方法可以做：
method1：放入一个数组，然后排序 NlogN N为个数
method2：heap做 NlogK N为元素个数，heap排序 O(log N)    也可以用于array的合并
time:nklogk   space:k
https://www.youtube.com/watch?v=XqA8bBoEdIY
method3: divide and conque  
"""

#method 2
class Solution:
    
    #first, we should overriding ListNode compare function __lt__to make customized compare happens: compare ListNode
    def __lt__(self, other):  
        return self.val < other.val
    
    ListNode.__lt__=__lt__ # overide the __lt__ function for ListNode
    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        hq = []
        for head in lists:
            if head:
                heappush(hq, head)
        
        dummynode = ListNode(0)
        curr = dummynode
        while len(hq) > 0:
            curr.next = heappop(hq)
            curr = curr.next
            if curr.next:
                heappush(hq, (curr.next))
        return dummynode.next
          
