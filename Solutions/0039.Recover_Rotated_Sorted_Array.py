/*
Description
Given a rotated sorted array, return it to sorted array in-place.（Ascending）

Wechat reply the 【39】 get the latest frequent Interview questions . (wechat id : jiuzhang15)

What is rotated array?

For example, the orginal array is [1,2,3,4], The rotated array of it can be [1,2,3,4], [2,3,4,1], [3,4,1,2], [4,1,2,3]
Example
Example 1:

Input:

array = [4,5,1,2,3]
Output:

[1,2,3,4,5]
Explanation:

Restore the rotated sorted array.

Example 2:

Input:

array = [6,8,9,1,2]
Output:

[1,2,6,8,9]
Explanation:

Restore the rotated sorted array.
*/

public class Solution {
    /**
     * @param nums: An integer array
     * @return: nothing
     */
    public void recoverRotatedSortedArray(List<Integer> nums) {
        // write your code here
        for (int i = 0; i < nums.size() - 1; i++) {
            if (nums.get(i) > nums.get(i + 1)) {
                reverse(nums, 0, i);
                reverse(nums, i + 1, nums.size() - 1);
                reverse(nums, 0, nums.size() - 1);
            }
        }
    }

    private void reverse(List<Integer> nums, int start, int end) {
        for (int i = start, j = end; i < j; i++, j--) {
            int temp = nums.get(i);
            nums.set(i, nums.get(j));
            nums.set(j, temp);
        }
    }
}



