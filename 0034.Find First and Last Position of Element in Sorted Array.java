/**
last position时
start < end的写法会导致死循环 dead loop
why？ 因为取中点除2的运算是偏左的
所以first+last整合成一个模板去写，所以start+1<end任何情况都成立，但是要做double check
**/

class Solution {
    public int[] searchRange(int[] nums, int target) {
        if (nums == null || nums.length == 0) {
            return new int[] {-1, -1};
        }
        
        int firstIndex = searchFirst(nums, target);
        if (firstIndex == -1) {
            return new int[]{-1, -1};
        }
        
        int lastIndex = searchLast(nums, target);
        
        return new int[]{firstIndex, lastIndex};
    }
    
    public int searchFirst(int[] nums, int target) {
        
        if (nums == null || nums.length == 0) {
            return -1;
        }
        
        int start = 0, end = nums.length - 1;
        while (start + 1 < end){
            int mid = (end - start)/2 + start;
            if (nums[mid] == target) {
                end = mid;
            } else if (nums[mid] < target) {
                start = mid;
            } else {                
                end = mid;
            }
        }
        
        if (nums[start] == target) {
            return start;
        }
        if (nums[end] == target) {
            return end;
        }
        
        return -1;
    }
    
    public int searchLast(int[] nums, int target) {
        if (nums == null || nums.length == 0) {
            return -1;
        }
        
        int start = 0, end = nums.length - 1;
        while (start + 1 < end) {
            int mid = (end - start)/2 + start;
            if (nums[mid] == target){
                start = mid;
            } else if (nums[mid] < target) {
                start = mid;
            } else {
                end = mid;
            }
        }
        
        if (nums[end] == target){
            return end;
        } 
        if (nums[start] == target) {
            return start;
        }
        
        return -1;
    }
    
}
