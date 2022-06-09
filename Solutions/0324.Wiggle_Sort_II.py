"""
Given an integer array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....

You may assume the input array always has a valid answer.

 

Example 1:

Input: nums = [1,5,1,1,6,4]
Output: [1,6,1,5,1,4]
Explanation: [1,4,1,5,1,6] is also accepted.
Example 2:

Input: nums = [1,3,2,2,3,1]
Output: [2,3,1,3,1,2]
 

Constraints:

1 <= nums.length <= 5 * 104
0 <= nums[i] <= 5000
It is guaranteed that there will be an answer for the given input nums.
 

Follow Up: Can you do it in O(n) time and/or in-place with O(1) extra space?
"""

"""
这题比Wiggle Sort I难在相邻的数不能相等，所以相邻交换法行不通，
我们可以sort the nums, then 把有序数组从中间分成两部分，然后从前半段的末尾取一个，
在从后半的末尾取一个，这样保证了第一个数小于第二个数，然后从前半段取倒数第二个，
从后半段取倒数第二个，这保证了第二个数大于第三个数，且第三个数小于第四个数，以此类推。
O(nlogn), O(n)
"""
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        temp = nums.copy()
        temp.sort()
        lens = len(temp)
        i, j = (lens - 1) // 2, lens - 1
        k = 0
        while i >= 0 and j > (lens - 1) // 2:
            nums[k] = temp[i]
            k += 1
            i -= 1
            nums[k] = temp[j]
            j -= 1
            k += 1
        while i >= 0:
            nums[k] = temp[i]
            k += 1
            i -= 1

"""
Follow Up: Can you do it in O(n) time and/or in-place with O(1) extra space?
O(n)的时间，O(1)额外空间 算法一言难尽，去上九章算法强化班吧。
这个问题的做法是，先找到中位数，然后根据中位数把数组分成三个部分，< median, == median, > median 然后把这三个部分按照从大到小摆放在从右到左每次跳一格的位置。
"""
class Solution:
    """
    @param: nums: A list of integers
    @return: nothing
    """
    def wiggleSort(self, nums):
        if not nums:
            return
        
        # partition nums into smaller half and bigger half
        # all nums in smaller half <= any num in bigger half
        median = self.find_median(nums)
        
        n = len(nums)

        # reorder the nums from
        # 0 => n-1(odd), (n-2)(even)
        # 1 => n-3
        # 2 => n-5
        # ...
        # (n - 1) / 2 => 0
        # (n - 1) / 2 + 1 => n - 2(odd), n - 1(even)
        # (n - 1) / 2 + 2 => n - 4(odd), n - 3(even)
        # ... 
        def get_index(i):
            if i <= (n - 1) // 2:
                return n - i * 2 - 1 - (n + 1) % 2
            i -= (n - 1) // 2 + 1
            return n - i * 2 - 1 - n % 2
            
        # 3-way partition
        left, i, right = 0, 0, n - 1
        while i <= right:
            if nums[get_index(i)] < median:
                nums[get_index(left)], nums[get_index(i)] = nums[get_index(i)], nums[get_index(left)]
                i += 1
                left += 1
            elif nums[get_index(i)] == median:
                i += 1
            else:
                nums[get_index(right)], nums[get_index(i)] = nums[get_index(i)], nums[get_index(right)]
                right -= 1
        
    def find_median(self, nums):
        return self.find_kth(nums, 0, len(nums) - 1, (len(nums) - 1) // 2)
    
    def find_kth(self, nums, start, end, kth):
        # k is zero based
        left, right = start, end
        mid = nums[(left + right) // 2]
        
        while left <= right:
            while left <= right and nums[left] < mid:
                left += 1
            while left <= right and nums[right] > mid:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left, right = left + 1, right - 1
                
        if kth <= right:
            return self.find_kth(nums, start, right, kth)
        elif kth >= left:
            return self.find_kth(nums, left, end, kth)
        else:
            return nums[kth]
