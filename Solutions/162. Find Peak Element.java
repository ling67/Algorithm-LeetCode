/**
we should consider 4 diff situation 
nums[0] > nums[1] nums[n] > nums[n-1]// nums[n] < nums[n-1] we consider 0 is the peak index
nums[0] < nums[1] nums[n] > nums[n-1] n is the peak index
nums[0] < nums[1] nums[n] < nums[n-1] keep consider 3 situation
**/

class Solution {
    public int findPeakElement(int[] nums) {
        if (nums == null || nums.length == 0 || nums.length == 1){
            return 0;
        }
        
        int n = nums.length;
        
        if (nums[0] > nums[1]) return 0;
        if (nums[n-1] > nums[n-2]) return n-1;
        
        int start = 0, end = n-1;
        while (start + 1 < end){
            
            if (nums[start] > nums[start+1]) {
                return start;
            }
            if (nums[end] >  nums[end-1]) {
                return end;
            }
            
            int mid = start + (end - start) / 2;
            
            if((nums[mid-1] < nums[mid]) && nums[mid] > nums[mid+1]) {
                return mid;
            } else if ((nums[mid-1] < nums[mid]) && (nums[mid] < nums[mid+1])) {
                start = mid;
            } else {
                end = mid;
            }
        }
        
        if (nums[start] > nums[end]) {
            return start;
        } else{
            return end;
        }
        
    }
}
