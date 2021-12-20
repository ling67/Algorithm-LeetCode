class Solution {
    public int findMin(int[] nums) {

        int n = nums.length;
        if (n == 1) {
            return nums[0];            
        }
        
        int start = 0, end = n-1;
        while ( start + 1 < end) {
            int mid = start + (end - start) / 2;
            if (nums[mid] <= nums[n-1] ){
                end = mid;
            } else {
                start = mid;
            }
        }
        if (nums[start] < nums[end]) {
            return nums[start];
        } else {
            return nums[end];
        }
        
    }
}
