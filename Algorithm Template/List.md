```python
a.Dummy Node <br>
如何使用 Dummy Node
head = dummy 这句话总是需要么? 
什么时候使用 Dummy Node? 结构变化，会导致头部变化，就可以用Dummy Node
Dummy Node 是否需要删除? 不用，Java会自动删除
使用 Dummy Node 算面试官会说我耗费了额外空间么? 
Dummy Node 非用不可么? 不是，写起来可能很麻烦
Dummy Node 初始化的值重要么?  不重要
链表的问题都需要用到 Dummy Node 么?  90%都可以用到
总结：链表的题一般就使用dummy node

1.求中点 <br>
slow = fast = head
slow = slow.next
fast = fast.next.next
最后slow是在中间或者中间偏右的。
但是归并排序，或者将链表分成二部分时，slow = head fast = head.next。因为对于归并排序，如果是2个元素后，slow=fast=head 会陷入拆分后还是2个元素。

2.求链表是否有环: Linked List Cycle  <br>
常规解法1：extra空间 用hashSet
非常规解法2：快慢指针  follow up:判断两个链表是不是有交集，并且求出相交点；
slow = fast = head
slow = slow.next
fast = fast.next.next
Then check if equal.

3.求链表的相交点：
两个链表连起来看有没有环，将一个链表的头尾相连，判断有没有环，有环说明是相交的，然后求出相交点。
先判断有没有交点：slow = fast = head slow每次走一步，fast每次走2步 
再求相交点：head slow分别出发，相遇点就是交点

特别注意：指针的题目特别注意有的地方要断开，有的地方链表已经变了
```

## Reverse Linked List 
```python

```

## 快慢find mid
```python

```

## 判断是否有环
```python
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
```

## 得到环的入口
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




