"""
Given an array of n elements, where each element is at most k away from its target position, devise an algorithm that sorts in O(n log k) time. 
For example, let us consider k is 2, an element at index 7 in the sorted array, can be at indexes 5, 6, 7, 8, 9 in the given array.
Examples:
Input : arr[] = {6, 5, 3, 2, 8, 10, 9}
            k = 3 
Output : arr[] = {2, 3, 5, 6, 8, 9, 10}
Input : arr[] = {10, 9, 8, 7, 4, 70, 60, 50}
         k = 4
Output : arr[] = {4, 7, 8, 9, 10, 50, 60, 70}
"""


    
"""
solution: 用一个大小为k的heapq存储k个元素，然后i从k开始遍历nums, 遍历的过程中每次都更新nums的最左边: nums[target_idx] = heappop(hq)，
同时更新hq: heappush(hq, nums[i]), 这么做成立的原因是i是从k开始遍历的，所以nums[i]一定是大于nums[0]的，而nums[0]>=heappop(hq), 
所以nums[i]及其后面的数一定是大于heappop(hq)的，所以可以放心地把heappop(hq)放到target_idx的位置。时间复杂度是O(nlogk). 
当k=1: O(0), 当k=n: O(nlogn). 当k=n时就degrade成了heap sort了
"""

from heapq import heapify, heappop, heappush

def sort_k(nums, k):
    hq = []
    for i in range(k):
        hq.append(nums[i])

    heapify(hq)

    target_idx = 0
    for i in range(k, len(nums)):
        nums[target_idx] = heappop(hq)
        target_idx += 1
        heappush(hq, nums[i])

    while hq:
        nums[target_idx] = heappop(hq)
        target_idx += 1

if __name__ == "__main__":
    k = 3
    arr = [2, 6, 3, 12, 56, 8]
    sort_k(arr, k)
    print(arr)
