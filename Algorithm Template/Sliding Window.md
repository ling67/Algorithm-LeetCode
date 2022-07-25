* A subarray is a contiguous part of the array.
* 只能用于全是正数的数组，要保证窗口移动过程中的单调性。 有负数可以使用prefix sum

## Sliding Window 第一种模板：Find Min_Window_Size for At Least Problem  （）

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

```python

* 和小于target的最小size

for j in range(lens):
    更新带有 j 的信息
    while i <= j and 满足条件:
        更新带有 i 的信息
        i += 1
    更新 res if 满足条件

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









