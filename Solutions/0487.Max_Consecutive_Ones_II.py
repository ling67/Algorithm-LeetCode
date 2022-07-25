"""
Given a binary array nums, return the maximum number of consecutive 1's in the array if you can flip at most one 0.

 

Example 1:

Input: nums = [1,0,1,1,0]
Output: 4
Explanation: Flip the first zero will get the maximum number of consecutive 1s. After flipping, the maximum number of consecutive 1s is 4.
Example 2:

Input: nums = [1,0,1,1,0,1]
Output: 4
 

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
"""

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_lens = 0
        zero_cnt = 0
        i = 0
        for j in range(len(nums)):
            zero_cnt += 1 if nums[j] == 0 else 0
            
            while i <= j and zero_cnt > 1:
                zero_cnt -= 1 if nums[i] == 0 else 0
                i += 1
            if zero_cnt <= 1:
                max_lens = max(max_lens, j - i + 1)
        return max_lens
            

"""
sliding window solution: find the longest subarray with at most one 0.
这题是most s problem, 写法是while loop里让前面的指针去追后面的指针. 
"""
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_lens = 0
        zero_flip = 0
        i = 0
        for j in range(len(nums)):
            if nums[j] == 0:
                zero_flip += 1
            
            while i <= j and zero_flip > 1:
                if nums[i] == 0:
                    zero_flip -= 1
                i += 1
            
            if zero_flip <= 1:
                max_lens = max(max_lens, j - i + 1)
        
        return max_lens
      
"""
Follow up:
What if the input numbers come in one by one as an infinite stream? 
In other words, you can't store all numbers coming from the stream as it's too large to hold in memory. 
Could you solve it efficiently?
"""
"""
In answering the follow up question, sliding window solution is not ideal, we use solution 2 which is quite smart!
"""
"""
solution 2: record prev_lens and curr_lens for the previous lens of consecutive 1s and curr lens of consecutive 1s.
update them we there is a new 0 coming, otherwise curr_lens += 1.
"""
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        prev_lens, curr_lens = -1, 0        # note that prev_lens is initialized to -1, meaning that we haven't seen any 0 yet
        max_lens = 0
        for num in nums:
            if num == 1:
                curr_lens += 1
            else:
                prev_lens, curr_lens = curr_lens, 0
            max_lens = max(max_lens, prev_lens + 1 + curr_lens)
        return max_lens
