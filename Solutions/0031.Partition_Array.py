/*
Description
Given an array nums of integers and an int k, partition the array (i.e move the elements in "nums") such that:

All elements < k are moved to the left
All elements >= k are moved to the right
Return the partitioning index, i.e the first index i nums[i] >= k.

You should do really partition in array nums instead of just counting the numbers of integers smaller than k.

If all elements in nums are smaller than k, then return nums.length
0 <= nums.length <= 20000<=nums.length<=2000

Example
Example 1:

Input:

nums = []
k = 9
Output:

0
Explanation:

Empty array, print 0.
*/

class Solution:
    """
    @param nums: The integer array you should partition
    @param k: An integer
    @return: The index after partition
    """
    def partitionArray(self, nums, k):
        # write your code here
        lens = len(nums)
        if lens == 0:
            return 0

        l, r = 0, lens - 1
        while l <= r:
            while l <= r and nums[l] < k:
                l += 1
            while l <= r and nums[r] >= k:
                r -= 1
            if l <= r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        
        return l
    

public class Solution {
    /**
     * @param nums: The integer array you should partition
     * @param k: An integer
     * @return: The index after partition
     */
    public int partitionArray(int[] nums, int k) {
        // write your code here
        if (nums == null || nums.length == 0) {
            return 0;
        }
        int left = 0, right = nums.length - 1;
        while (left <= right) {   //判断1
            while ((left <= right) && (nums[left] < k)) { //判断2
                left++;
            }
            while ((left <= right) && nums[right] >= k) { //判断3
                right--;
            }
            if (left <= right) {  //判断4 这四句判断一定要写的一样
                int temp = nums[left];
                nums[left] = nums[right];
                nums[right] = temp;
                left++;
                right--;
            }
        }
        return left;
    }
}




