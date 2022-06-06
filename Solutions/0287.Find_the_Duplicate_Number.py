"""
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.

 

Example 1:

Input: nums = [1,3,4,2,2]
Output: 2
Example 2:

Input: nums = [3,1,3,4,2]
Output: 3
 

Constraints:

1 <= n <= 105
nums.length == n + 1
1 <= nums[i] <= n
All the integers in nums appear only once except for precisely one integer which appears two or more times.
"""

"""
九章算法强化班中讲过的基于值的二分法。 这个题比较好的理解方法是画一个坐标轴：
x轴是 0, 1, 2, ... n。
y轴是对应的 <=x 的数的个数，比如 <=0 的数的个数是0，就在（0,0）这个坐标画一个点。<=n 的数的个数是 n+1 个，就在 (n,n+1)画一个点。
O(nlogn)
"""
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        start, end = 1, len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if self.count(nums, mid) <= mid:
                start = mid
            else:
                end = mid
        return end if self.count(nums, start) <= start else start
    
    def count(self, nums, mid):
        cnt = 0
        for item in nums:
            if item <= mid:
                cnt += 1
        return cnt

"""
使用九章算法班&九章算法强化版里讲过的快慢指针的方法。 要做这个题你首先需要去做一下 Linked List Cycle 这个题。 如果把数据看做一个 LinkedList，第 i 个位置上的值代表第 i 个点的下一个点是什么的话，我们就能画出一个从 0 出发的，一共有 n + 1 个点的 Linked List。 可以证明的一件事情是，这个 Linked List 一定存在环。因为无环的 Linked List 里 非空next 的数目和节点的数目关系是差一个（节点多，非空next少）
那么，我们证明了这是一个带环链表。而我们要找的重复的数，也就是两个点都指向了同一个点作为 next 的那个点。也就是环的入口。
因此完全套用 Linked List Cycle 这个题快慢指针的方法即可。
什么是快慢指针算法？ 从起点出发，慢指针走一步，快指针走两步。因为有环，所以一定会相遇。 相遇之后，把其中一根指针拉回起点，重新走，这回快慢指针都各走一步。他们仍然会再次相遇，且相遇点为环的入口。
时间复杂度是多少？ 时间复杂度是O(n)的。
"""
"""
[1,5,3,6,2,2,4]
1 -> 5 -> 2 -> 3 -> 6 -> 4 -> 2.... 形成了环
可以把这个数组的每一个数num看成这样一个linked list node: num的下标代表.val, num的值代表.next指向下一个node。
那么如果存在重复的num，那就表示有两个不同node都指向了同一个node，也就是成环的地点。这么想这个题目就和142一样了
"""
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # step 1: 快慢指针找到相遇的点
        slowNum, fastNum = 0, 0
        while True:
            slowNum = nums[slowNum]
            fastNum = nums[nums[fastNum]]
            if slowNum == fastNum:
                break
            
        # step 2: 重新定义两个指针p1, p2分别从head和上面相遇的点出发，p1, p2相遇的点就是环的入口
        currNum = 0
        while True:
            currNum = nums[currNum]
            slowNum = nums[slowNum]
            if currNum == slowNum:
                return currNum
