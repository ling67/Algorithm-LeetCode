"""
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2

Constraints:

1 <= nums.length <= 2 * 104
-1000 <= nums[i] <= 1000
-107 <= k <= 107
"""

"""
我们先构造一个数组pre_sum, 然后接下来就和two sum problem是一样的了，
two sum是寻找两数之和：nums[i]+nums[j] = k, 这里是寻找两数之差：pre_sum[j] - pre_sum[i] = k. 
方法都是用hashmap记录访问过的nums[i], O(N), O(N)
"""
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pre_sum_dict = defaultdict(int)  #pre_sum --> cnt of the occurance of the pre_sum
        pre_sum_dict[0] = 1  #特别注意pre_sum_dict需要初始化！！！和为0的数量为1
        
        # Our problem is: find how many pairs of <i,j> satisfies prefix_sum[j] - prefix_sum[i] == k?
        #接下来是two sum问题
        pre_sum = 0
        cnt = 0
        for i, num in enumerate(nums):
            pre_sum += num  # 这里的pre_sum相当于prefix_sum[j+1], 一般都不会单独开一个数组出来存prefix_sum
            if pre_sum - k in pre_sum_dict:  # 等价于if prefix_sum[j] - prefix_sum[i] == k
                cnt += pre_sum_dict[pre_sum - k]
                
            pre_sum_dict[pre_sum] += 1   # 将 pre_sum 存入pre_sum_dict中
    
        return cnt
            
        
