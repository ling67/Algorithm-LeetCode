"""
Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.

Since the result may be very large, so you need to return a string instead of an integer.

 

Example 1:

Input: nums = [10,2]
Output: "210"
Example 2:

Input: nums = [3,30,34,5,9]
Output: "9534330"
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 109
"""

class Compare(str):
    def __lt__(x, y):
        return x + y < y + x
    
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        largest_num = ''.join(sorted(map(str, nums), key=Compare, reverse = True))    
        return '0' if largest_num[0] == '0' else largest_num   #所有数字为0，就返回0 
        
#map(str, nums) means for each num in nums, excute str() function, return  a list of the results after applying the given function to each item of a given iterable (list, tuple etc.) 

