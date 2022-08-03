"""
We are given hours, a list of the number of hours worked per day for a given employee.

A day is considered to be a tiring day if and only if the number of hours worked is (strictly) greater than 8.

A well-performing interval is an interval of days for which the number of tiring days is strictly larger than the number of non-tiring days.

Return the length of the longest well-performing interval.

 

Example 1:

Input: hours = [9,9,6,0,6,6,9]
Output: 3
Explanation: The longest well-performing interval is [9,9,6].
Example 2:

Input: hours = [6,6,6]
Output: 0
 

Constraints:

1 <= hours.length <= 104
0 <= hours[i] <= 16
"""

#Solution 1: brute force  O(n^2)
class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        max_len = 0
        for i in range(len(hours)):
            tiring_cnt = 0
            non_tiring_cnt = 0
            for j in range(i, len(hours)):
                if hours[j] > 8:
                    tiring_cnt += 1
                else:
                    non_tiring_cnt += 1
                
                if tiring_cnt > non_tiring_cnt:
                    max_len = max(max_len, j - i + 1)
                    
        return max_len
      
# Solution 2: prefix_sum
"""
step 1: 大于8小时的工作时间定义为1， 小于定义为-1， 这样就得到了一个nums，
step 2: now the problem is to find the longest subarray with sum > 0. 
since there is negative numbers, we cannot use sliding window, for subarray sum at least/most k problem with negative number, we use prefix sum + mono deque. 
因为这一题我们只需要check pre_sum - 1 in pre_sum_dict. 所以其实是一个subarray sum equals k problem. 
For subarray sum equals k problem with negative number, we use prefix sum + hashmap. 
问题：为什么我们只check pre_sum - 1 in pre_sum_dict, 而不去check all possible pre_sum - x?
因为 pre_sum - x 并不需要关心, 因为如果是最长子数组, 子数组的和一定是1, 所以只用关心 pre_sum - 1. 
感觉这个表述有点问题, 因为我们还判断了if pre_sum > 0，所以才成立的
"""

class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        nums = [1 if hours[i] > 8 else -1 for i in range(len(hours))]
        # now the problem is to find the longest subarray with sum > 0.
        
        pre_sum = 0
        pre_sum_dict = collections.defaultdict(int)     # pre-sum --> the idx the pre_sum occured
        pre_sum_dict[0] = -1
        res = 0
        for i, num in enumerate(nums):
            pre_sum += num
            
            if pre_sum > 0:     # if pre_sum is aleady positive, that means it is well-performing from 0 to i
                res = i + 1
            else:               # if pre_sum is not positive, then we need to find an previous idx,
                if pre_sum - 1 in pre_sum_dict:         # so that pre_sum - that pre_sum[idx] is at least 1
                    res = max(res, i - pre_sum_dict[pre_sum - 1])
            
            if pre_sum not in pre_sum_dict:     # we only store the first appearance of the pre_sum
                pre_sum_dict[pre_sum] = i
                
        return res
