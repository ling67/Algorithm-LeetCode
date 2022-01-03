/*
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.


Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

*/

class Solution {
    public void sortColors(int[] nums) {
        int left = 0, right = nums.length - 1, index = 0;
        //left的左边都是0，right的右边都是2
        while (index <= right) {
            if (nums[index] == 0) {
                //交换
                int temp = nums[index];
                nums[index] = nums[left];
                nums[left] = temp;
                index++;
                left++;
            } else if(nums[index] == 1) {
                index++;
            } else {
                //交换
                int temp = nums[index];
                nums[index] = nums[right];
                nums[right] = temp;
                //index++;  //注意很容易错！index不++的原因是因为与right交换之后，可能把2交换到了index那里，如果这时候index++的话，name这个2就永远都定在那里了，所以需要index不动，目的是为了再访问这个被交换的2一次
                right--;
            }
        }
    }
}

