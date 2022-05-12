Given a circular integer array nums (i.e., the next element of nums[nums.length - 1] is nums[0]), return the next greater number for every element in nums.

The next greater number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, return -1 for this number.

 

Example 1:

Input: nums = [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2; 
The number 2 can't find next greater number. 
The second 1's next greater number needs to search circularly, which is also 2.
Example 2:

Input: nums = [1,2,3,4,3]
Output: [2,3,4,-1,4]
 

Constraints:

1 <= nums.length <= 104
-109 <= nums[i] <= 109

"""
1.求数组中右边第一个比当前值大的数，套用模板，要么单调递增栈，要么单调递减栈
2.最后一个的下一个是第一个，所以扩充数组*2
3.大于栈顶元素就出栈，小于就入栈
"""
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        st = [] #单调递减栈,存(num, index)
        res = [-1 for _ in range(n*2)]
        nums = nums + nums  #最后一个的下一个是第一个，所以扩充数组*2
        for index, num in enumerate(nums):  #enumerate使用容易忘记
            while len(st) > 0 and st[-1][0] < num:  #注意存的是tuple
                mapping = st.pop()
                res[mapping[1]] = num
            st.append((num, index))
        
        return res[:n]
