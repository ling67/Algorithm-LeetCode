# 滑动窗口

题目暴力解法当然是 两个for循环，然后不断的寻找符合条件的子序列，时间复杂度很明显是O(n^2)。



* A subarray is a contiguous part of the array.
* A substring is a contiguous sequence of characters within a string.
* 只能用于全是正数的数组，要保证窗口移动过程中的单调性。 有负数可以使用prefix sum。



接下来就开始介绍数组操作中另一个重要的方法：**滑动窗口**。

所谓滑动窗口，**就是不断的调节子序列的起始位置和终止位置，从而得出我们要想的结果**。

在暴力解法中，是一个for循环滑动窗口的起始位置，一个for循环为滑动窗口的终止位置，用两个for循环 完成了一个不断搜索区间的过程。 

那么滑动窗口如何用一个for循环来完成这个操作呢。 

首先要思考 如果用一个for循环，那么应该表示 滑动窗口的起始位置，还是终止位置。 

如果只用一个for循环来表示 滑动窗口的起始位置，那么如何遍历剩下的终止位置？ 

此时难免再次陷入 暴力解法的怪圈。 

所以 只用一个for循环，那么这个循环的索引，一定是表示 滑动窗口的终止位置。 

那么问题来了， 滑动窗口的起始位置如何移动呢？ 

这里还是以题目中的示例来举例，s=7， 数组是 2，3，1，2，4，3，来看一下查找的过程：

<img src="https://code-thinking.cdn.bcebos.com/gifs/209.%E9%95%BF%E5%BA%A6%E6%9C%80%E5%B0%8F%E7%9A%84%E5%AD%90%E6%95%B0%E7%BB%84.gif" width="350">

最后找到 4，3 是最短距离。

其实从动画中可以发现滑动窗口也可以理解为双指针法的一种！只不过这种解法更像是一个窗口的移动，所以叫做滑动窗口更适合一些。

在本题中实现滑动窗口，主要确定如下三点：

* 窗口内是什么？
* 如何移动窗口的起始位置？
* 如何移动窗口的结束位置？

窗口就是 满足其和 ≥ s 的长度最小的 连续 子数组。

窗口的起始位置如何移动：如果当前窗口的值大于s了，窗口就要向前移动了（也就是该缩小了）。

窗口的结束位置如何移动：窗口的结束位置就是遍历数组的指针，也就是for循环里的索引。

解题的关键在于 窗口的起始位置如何移动，如图所示：

<img src="https://img-blog.csdnimg.cn/20210312160441942.png" width="550">

可以发现**滑动窗口的精妙之处在于根据当前子序列和大小的情况，不断调节子序列的起始位置。从而将O(n^2)暴力解法降为O(n)。**


## Sliding Window 第一种模板：Find Min_Window_Size for At Least Problem

* 和大于等于target的最小size
* i不变，j往前走直到满足条件，i往前走一步，j继续往前走直到满足条件

```python

for i in range(lens):
    while j < lens and 满足条件:
        更新带有 j 的信息
        j += 1
    更新 res if 满足条件
    更新带有 i 的信息

Leetcode: 209

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float("inf")
        sums = 0
        i = 0
        for j in range(len(nums)):
            sums += nums[j]
            while sums >= target:
                res = min(res, j - i + 1)
                sums -= nums[i]
                i += 1
        return 0 if res == float("inf") else res

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        lens = len(nums)
        minSize = float("inf")
        sums = 0
        j = 0
        for i in range(lens):
            while j < lens and sums < target:    # 满足条件 sums < s
                sums += nums[j]                  # 更新 j
                j += 1
            if sums >= target:                  # 更新 res if 满足条件
                minSize = min(minSize, j - i)  
                
            sums -= nums[i]                     # 更新 i
            
        return minSize if minSize != float("inf") else 0
        
```

## Sliding Window 第二种模板：Find Max_Window_Size for At Most Problem   

* 和小于target的最小size

```python
for j in range(lens):
    更新带有 j 的信息
    while i <= j and 满足条件:
        更新带有 i 的信息
        i += 1
    更新 res if 满足条件
```

```python
Leetcode: 1208

class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        i = 0
        sums = 0
        max_lens = 0
        for j in range(len(s)):
            sums += abs(ord(t[j]) - ord(s[j]))
            if sums <= maxCost:
                max_lens = max(max_lens, j - i + 1)
            else:
                sums -= abs(ord(t[i]) - ord(s[i]))
                i += 1
        return max_lens
```

```python
Leetcode: 930

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        return self._at_most(nums, goal) - self._at_most(nums, goal - 1)
    
    def _at_most(self, nums, target):
        cnt = 0
        sums = 0
        i = 0
        for j in range(len(nums)):
            sums = sums + nums[j]
            
            while i < j and sums > target:
                sums = sums - nums[i]
                i += 1
                
            if sums <= target:
                cnt += j - i + 1  #以j结尾连续字串的个数
                
        return cnt
```

## Sliding Window 第三种模板是 fixed_window problem

```python
写法是while loop里让前面的指针去追后面的指针. 模板：

for i in range(lens):
    把 ith item 加到window
    if i >= k:
        把 (i-k)th item 吐出来 to maintian a fixed size window
更新 res if 满足条件


"""
567
permutation:排列，顺序不一样
solution 1: 由于我们要求的substring时固定长度的，所以最好maintina a fixed size window - 套用fix window模板
"""
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)   #store s1的长度
        cnter_2 = Counter(s1)   #store s1的字符和频次
        ch_to_cnt = defaultdict(int)   #记录窗口内的字母和频次的对应关系
        
        for i in range(len(s2)):
            ch_to_cnt[s2[i]] += 1
            
            if i >= k:
                ch_to_cnt[s2[i - k]] -= 1
                if ch_to_cnt[s2[i - k]] == 0:
                    del ch_to_cnt[s2[i - k]]
            
            if ch_to_cnt == cnter_2:
                return True
            
        return False

```









