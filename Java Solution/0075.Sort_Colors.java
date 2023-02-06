// Solution: 3 point
class Solution {
    public void sortColors(int[] nums) {
        int left = 0, right = nums.length - 1, index = 0;
        //left的左边都是0，right的右边都是2
        while (index <= right) {        //容易错，index <= right
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
