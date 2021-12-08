/**
符号两边的数据都要有空格 sum = start + end
while-if后面的括号也要有空格 if () {}
为啥老丁写的只写2个分支？
重点：
start + 1 < end 
start + (end - start) / 2 
A[mid] ==, <, >  mid
A[start] A[end] ? target
*/

class Solution {
    public int search(int[] nums, int target) {
        if (nums == null || nums.length == 0) {
            return -1;
        }
        
        int start = 0, end = nums.length - 1;
        
        while (start + 1 < end) {
            int mid = start + (end - start) / 2;
            if (nums[mid] == target){
                return mid;
            } else if(nums[mid] < target){
                start = mid;
            } else{
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
}

