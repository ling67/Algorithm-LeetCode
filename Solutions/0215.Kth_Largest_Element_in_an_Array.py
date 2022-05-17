/*
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

 

Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4

*/

//python heap
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapify(nums)    #初始化成最小堆
        while len(nums) > k:
            heappop(nums)
        return nums[0]
       
//python quick select
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums or k < 1 or k > len(nums):
            return None
        
        return self.quick_select(nums, 0, len(nums) - 1, len(nums) - k)
    
    def quick_select(self, nums, start, end, k):
        if start == end:    #模板注意点1，跟sort排序不一样
            return nums[k]
        
        left, right = start, end
        pivot = nums[(start + end) // 2]
        while left <= right:    # 模板注意点2
            while left <= right and nums[left] < pivot:    # 模板注意点3
                left += 1
            while left <= right and nums[right] > pivot:
                right -= 1 
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        if k <= right:      # 模板注意点4
            return self._quick_select(nums, start, right, k)
        elif k >= left:     # 模板注意点5
            return self._quick_select(nums, left, end, k)
        else:
            return nums[k]
       
//java version
class Solution {
    public int findKthLargest(int[] nums, int k) {
        int n = nums.length;
        if (k > n) {
            return 0;
        }
        PriorityQueue<Integer> heap = new PriorityQueue<>();   //此队列的头 是按指定排序方式确定的最小元素
        for (int i = 0; i < n; i++) {
            heap.offer(nums[i]);
        }
        
        for (int i = 0; i < n - k; i++) {
            heap.poll();
        }

        return heap.peek();
    }
}



