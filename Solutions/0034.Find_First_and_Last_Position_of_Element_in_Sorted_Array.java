/**
last position时
start < end的写法会导致死循环 dead loop
why？ 因为取中点除2的运算是偏左的
所以first+last整合成一个模板去写，所以start+1<end任何情况都成立，但是要做double check
**/

"""
find the first value 
find the last value
2 time binary search
"""
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        
        #find the first index value
        start, end = 0, len(nums) - 1
        first, last = -1, -1
        while start + 1 < end:
            mid = start +  (end - start) // 2
            if nums[mid] >= target:
                end = mid
            else:
                start = mid
        
        
        if nums[end] == target:
            first = end
            
        if nums[start] == target:  ## 注意由于是想找first position of target，所以把start放在后面更新，这样如果出现nums[end]和nums[start]都等于target的情况的话，first可以被后面较小的start替换掉。
            first = start    
        
        #find the last index value
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = start +  (end - start) // 2
            if nums[mid] <= target:
                start = mid
            else:
                end = mid
        
        
        if nums[start] == target:
            last = start
        if nums[end] == target:
            last = end
            
        return [first, last]



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
