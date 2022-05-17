Skip to content
Search or jump to…
Pull requests
Issues
Marketplace
Explore
 
@jim0607 
jim0607
/
Leetcode
Private template
Code
Issues
Pull requests
Actions
Projects
Security
Insights
Settings
Leetcode/Solutions/Google__BinarySearchable.py /
@jim0607
jim0607 Create Google__BinarySearchable.py
Latest commit e8b87c8 on Jun 17, 2020
 History
 1 contributor
46 lines (40 sloc)  2.2 KB
   
Given an unordered array, how many integers would a binary search find? // TODO: prove the stack approach is accessible or not
Binary search is a search algorithm usually used on a sorted sequence to quickly find an element with a given value. 
In this problem we will evaluate how binary search performs on data that isn't necessarily sorted. 
An element is said to be binary searchable if, regardless of how the pivot is chosen the algorithm returns true. For example:
[2, 1, 3, 4, 6, 5] and target = 5, we cannot find 5. Because when the pivot is postion 4, we get element 6,
in binary search, we compare the pivot with target, and find that the pivot is larger than the target, we then drop right,
so we'll lose the opportunity to find target 5.
[2, 1, 3, 4, 5, 6] and target = 5, we can find 5. Because wherever we choose the pivots, we'll find target at last.
Given an unsorted array of n distinct integers, return the number of elements that are binary searchable.
Example 1:
Input: [1, 3, 2]
Output: 1
Explanation: However we choose the pivots, we will always find the number 1 when looking for it. This does not hold for 3 and 2.
所以要满足的条件是：前面的数都比他小，后面的数都比他大
因为如果前面有一个数比他大，这个数作为pivot的时候就会drop右边从而把这个数drop出去。
"""
solution: 左扫一遍，新建数组left_max[i]记录左边到i为止的最大值；然后右扫一遍，right_min[i]记录右边为止的最小值
再扫一遍，如果left_max[i] < nums[i] < right_min[i]就说明找到一个nums[i]是符合条件的
"""

def canBinarySearch(nums):
    """
    :param nums: un-sorted arr
    :return: how many num can be binary searched
    """
    left_max = [nums[0]] * len(nums)
    for i in range(1, len(nums)):
        left_max[i] = max(nums[i], left_max[i - 1])

    right_min = [nums[-1]] * len(nums)
    for j in range(len(nums) - 2, -1, -1):
        right_min[j] = min(nums[j], right_min[j + 1])

    cnt = 0
    for i in range(len(nums)):
        if left_max[i] <= nums[i] <= right_min[i]:
            cnt += 1

    return cnt

if __name__ == "__main__":
    arr = [2, 1, 3, 4, 5, 6]
    res = canBinarySearch(arr)
    print(res)

也可以用单调栈，也是O(n)
© 2022 GitHub, Inc.
Terms
Privacy
Security
Status
Docs
Contact GitHub
Pricing
API
Training
Blog
About
