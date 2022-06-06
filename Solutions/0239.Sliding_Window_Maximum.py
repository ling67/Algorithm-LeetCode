"""
You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

 

Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Example 2:

Input: nums = [1], k = 1
Output: [1]
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
1 <= k <= nums.length
"""

"""
算法一 暴力
暴力枚举每个窗口，然后遍历一遍寻找最值，复杂度O(NK)
N是数组长度 K是窗口大小 这样我们做完一个窗口的结果就会扔掉它，然后去求下一个窗口的答案，这样不免有些浪费，毕竟两个相邻的窗口的元素差异是很小的，
我们如何来尽量的保留第一个窗口的答案呢？让第一个窗口的努力不会“白费”，这就需要我们的算法二单调队列
"""

"""
单调队列中的元素是严格单调的。我们在求解这个问题的时候需要维护他的单调性。
队首元素即为当前位置的最大值。假设要求滑动窗口中的最大值。我们就需要确保滑动窗口中的元素从队首到队尾是递减的。
每滑动一次就判断当前元素和队尾元素的关系，如果放入队尾满足单调递减，那么放入即可；如果放入不满足，就需要删除队尾元素直到放入当前元素之后满足队列单调递减。同时要确保已经出窗口的最大值（队首元素）被删除掉
"""
class Solution:
    """
    @param nums: A list of integers.
    @param k: An integer
    @return: The maximum number inside the window at each moving.
    """
    def maxSlidingWindow(self, nums, k):
        # write your code here
        # 答案数组
        ans = []
        # 单调队列
        qmax = collections.deque()
        # 队列里元素数量
        cnt = 0
        n = len(nums)
        for i in range(n):
            # 维护单调性
            while cnt != 0 and nums[i] > nums[qmax[-1]]:
                qmax.pop()
                cnt -= 1
            # 滑动窗口的长度超过了k 删掉超过的部分
            if cnt != 0 and i - qmax[0] >= k:
                qmax.popleft()
                cnt -= 1
            qmax.append(i)
            cnt += 1
            if i >= k - 1:
                ans.append(nums[qmax[0]])
            # print(qmax)
        return ans
      
"""
单调的双端队列
"""
from collections import deque


class Solution:
    """
    @param: nums: A list of integers
    @param: k: An integer
    @return: The maximum number inside the window at each moving
    """
    def maxSlidingWindow(self, nums, k):
        if not nums or not k:
            return []
            
        dq = deque([])
        
        for i in range(k - 1):
            self.push(dq, nums, i)
        
        result = []
        for i in range(k - 1, len(nums)):
            self.push(dq, nums, i)
            result.append(nums[dq[0]])
            if dq[0] == i - k + 1:
                dq.popleft()
                
        return result
            
    def push(self, dq, nums, i):
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()
        dq.append(i)


