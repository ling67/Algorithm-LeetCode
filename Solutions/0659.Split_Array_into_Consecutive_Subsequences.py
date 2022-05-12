"""
You are given an integer array nums that is sorted in non-decreasing order.

Determine if it is possible to split nums into one or more subsequences such that both of the following conditions are true:

Each subsequence is a consecutive increasing sequence (i.e. each integer is exactly one more than the previous integer).
All subsequences have a length of 3 or more.
Return true if you can split nums according to the above conditions, or false otherwise.

A subsequence of an array is a new array that is formed from the original array by deleting some (can be none) of the elements without disturbing the relative positions of the remaining elements. (i.e., [1,3,5] is a subsequence of [1,2,3,4,5] while [1,3,2] is not).

 

Example 1:

Input: nums = [1,2,3,3,4,5]
Output: true
Explanation: nums can be split into the following subsequences:
[1,2,3,3,4,5] --> 1, 2, 3
[1,2,3,3,4,5] --> 3, 4, 5
Example 2:

Input: nums = [1,2,3,3,4,4,5,5]
Output: true
Explanation: nums can be split into the following subsequences:
[1,2,3,3,4,4,5,5] --> 1, 2, 3, 4, 5
[1,2,3,3,4,4,5,5] --> 3, 4, 5
Example 3:

Input: nums = [1,2,3,4,4,5]
Output: false
Explanation: It is impossible to split nums into consecutive increasing subsequences of length 3 or more.
 

Constraints:

1 <= nums.length <= 104
-1000 <= nums[i] <= 1000
nums is sorted in non-decreasing order.
"""

"""
这道题我们遍历nums的时候只要当前的num被前面的顺子需要，就把num连上去，顺子连得越长越好。greedy所在
使用2个hashmap，第一个用来建立数字和次数的映射
第二个用来简历数字是否可以被前面顺子所需要
"""
class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        cnter = Counter(nums)  #store num and frequency
        can_append = defaultdict(int)
        for num in nums:
            #判断当前num还有没有,没有了直接跳过
            if cnter[num] == 0:
                continue
            
            #如果能够连接到前面的数组，就连上去
            if can_append[num] > 0:
                cnter[num] -= 1
                can_append[num] -= 1
                can_append[num + 1] += 1
                
            #不能连上前面数组，就新开一个数组   
            else: 
                for i in range(3):
                    if cnter[num + i] == 0:
                        return False
                    cnter[num + i] -= 1
                can_append[num + 3] += 1
        
        return True
                
