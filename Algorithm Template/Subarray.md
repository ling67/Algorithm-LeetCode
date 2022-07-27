
前缀和prefixSum[i]: the sum of all the items before i (not include i)

arr =           [1, 2, 3, 2]
prefixSum = [0, 1, 3, 6, 8]，构造prefixSum需要O(N)时间和O(N)空间

Remember: len(prefixSum) == len(arr) + 1
subArray的和就是sum(i~j包括i和j) = prefixSum[j+1] - prefixSum[i]，这样求任何一个subarray的和的时候只需要O(1)的时间复杂度就可以了!

subarray问题的模板：一般都是prefixSum+hashmap来实现，prefixSum记录遍历到的那个地方之前所有的item加起来的和。
hashmap的key是prefixSum，val是prefixSum中出现的数字频率（560. Subarray Sum Equals K, prefixSumMap = {0: 1}）
或者val是j/position (523. Continuous Subarray Sum, prefixSumMap = {0: -1}   key: prefixSum[j], val: j/position)
或者key是prefixSum[j]%K (974. Subarray Sums Divisible by K, prefixSum_f = {0: 1}   key: prefixSum[j]%K, val: 出现的frequency)

几乎所有的subArr的问题都是一样的模板，要背熟。	
一般的prefixSum[i]都是这样写的，而不是单独开一个数组出来存prefixSum:
for num in nums:
    prefixSum += num


```python
leetcode 53

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #step1:构造前缀和pre_sum
        pre_sum = [0 for _ in range(len(nums) + 1)]
        for i, num in enumerate(nums):
            pre_sum[i + 1] = pre_sum[i] + num
        
        #step2:the same as 127.best time to buy and sell stock
        min_pre = float("inf")
        max_sum = float("-inf")
        for pre in pre_sum:
            max_sum = max(max_sum, pre - min_pre)     # 注意不能更换maxSubSum和minPrefixSum的更新顺序,why， 比如输入为[-1]
            min_pre = min(min_pre, pre)
        return max_sum

```




