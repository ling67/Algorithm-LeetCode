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


## 滑动窗口题型

一般情况，子串问题，如什么最小覆盖子串、长度最小的子数组等等，都可以考虑使用滑动窗口算法。比较经典的滑动窗口题目有这些：

* 无重复字符的最长子串
* 最小覆盖子串
* 串联所有单词的子串
* 至多包含两个不同字符的最长子串
* 长度最小的子数组
* 滑动窗口最大值
* 字符串的排列
* 最小窗口子序列

## Sliding Window 第一种模板：Find Min_Window_Size for At Least Problem(求最小窗口)

* 和大于等于target的最小size
* i不变，j往前走直到满足条件，i往前走一步，j继续往前走直到满足条件

```python

Leetcode: 209

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float("inf")
        sums = 0
        i = 0
        for j in range(len(nums)):
            sums += nums[j]
            
            #满足条件更新res，移动i
            while sums >= target:
                res = min(res, j - i + 1)
                sums -= nums[i]
                i += 1
                
        return 0 if res == float("inf") else res
        
```

## Sliding Window 第二种模板：Find Max_Window_Size for At Most Problem(求最大窗口)

* 和小于target的最小size

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
            
            #不满足条件
            while i < j and sums > target:
                sums = sums - nums[i]
                i += 1
                
            #满足条件    
            if sums <= target:
                cnt += j - i + 1  #以j结尾连续字串的个数
                
        return cnt
```

## Sliding Window 第三种模板是 fixed_window problem (求固定窗口)

```python
写法是while loop里让前面的指针去追后面的指针. 模板：

for i in range(lens):
    把 ith item 加到window
    if i >= k:
        把 (i-k)th item 吐出来 to maintian a fixed size window
    if 满足条件：    
        更新 res
return

leedcode 1423
#滑动窗口:模板
 class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        size = n - k
        total = sum(cardPoints)
        min_points = total
        points = 0
        for i in range(len(cardPoints)):
            points += cardPoints[i]
            
            if i >= size:
                points -= cardPoints[i - size]
                
            if i >= size - 1:          #容易忘记
                min_points = min(min_points, points)
        
        return total - min_points

```

