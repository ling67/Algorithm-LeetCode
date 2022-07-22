## Reverse Linked List 
```python
递归
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        nextNode = head.next
        reversedHead = self.reverseList(nextNode)
        nextNode.next = head
        head.next = None
        
        return reversedHead 
```

```python
非递归
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        prev, curr = None, head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        return prev 
```

## 快慢指针求中点
```python
中间偏右：
slow = fast = head
slow = slow.next
fast = fast.next.next

中间偏左：
slow = head fast = head.next
但是归并排序，或者将链表分成二部分时，slow = head fast = head.next。因为对于归并排序，如果是2个元素后，slow=fast=head 会陷入拆分后还是2个元素。
```

## 判断是否有环
```python
常规解法1：extra空间 用hashSet
非常规解法2：快慢指针  follow up:判断两个链表是不是有交集，并且求出相交点；
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        slow = fast = head     #区别中间偏右
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
```

## 求环的入口
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        
        #快慢指针找到相遇的点
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
                
        #如果没有相遇，那就return None
        if slow != fast:
            return None
        
        #定义两根指针分别从head和上面相遇的点出发，然后p1, p2相遇的地方就是环的入口
        curr = head
        while curr != slow:     #易错点：一定要先判断curr! = slow
            curr = curr.next
            slow = slow.next
        return curr
```




