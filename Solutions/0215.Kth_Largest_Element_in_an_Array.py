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

#solution 0: heapq, time: O(N + KlogK), N 来自于for循环，logK来自于heap的长度是K，heap 的push 和pop都是logK; heapq适合做第K大，第K小，前K大，前K小问题;
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        numsHeapq = []
        for num in nums:
            heapq.heappush(numsHeapq, num)
            if len(numsHeapq) > k:
                heapq.heappop(numsHeapq)   # python默认是最小堆, 每次都是pop出最小值, 于是留下来的就是最大值了
        return numsHeapq[0]
    
#solution 1: heapq, time: O(N+NlogN)

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapify(nums)    #初始化成最小堆
        while len(nums) > k:
            heappop(nums)
        return nums[0]
       
#Solution2: quick select:O(N) - O(N^2)

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.quickSelect(nums, 0, len(nums) - 1, k - 1)
    
    def quickSelect(self, nums, start, end, k):
        if start == end:
            return nums[start]
        
        left, right = start, end
        pivot = nums[(left + right) // 2]
        
        while left <= right:
            while left <= right and nums[left] > pivot:
                left += 1
            while left <= right and nums[right] < pivot:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
                
        if k <= right:
            return self.quickSelect(nums, start, right, k)
        elif left <= k:
            return self.quickSelect(nums, left, end, k);
        else:
            return nums[k];

         
/****************************************java version************************************************/

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



