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

