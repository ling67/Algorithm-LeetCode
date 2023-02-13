class Solution {
    public int search(int[] nums, int target) {
        int l = 0, r = nums.length - 1;
        while (l + 1 < r) {
            int mid = l + (r - l) / 2;
            if (nums[mid] == target) {
                return mid;
            } 
            if (nums[l] <= nums[mid]) {
                if (nums[l] <= target && target < nums[mid]) {
                    r = mid;
                } else {
                    l = mid;
                }
            } else {
                if (nums[mid] < target && target <= nums[r]) {
                    l = mid;
                } else {
                    r = mid;
                }
            }
        }
        if (nums[l] == target) {
            return l;
        }

        if (nums[r] == target) {
            return r;
        }
        return -1;
    }
}
