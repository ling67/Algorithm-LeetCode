/*
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

*/

"""find the kth smallest element
O(log(M+N)), O(log(M+N))"""

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        lens = len(nums1) + len(nums2)
        if lens % 2 == 1:
            return self.kthSmallest(nums1, nums2, lens//2)
        else:
            return ( self.kthSmallest(nums1, nums2, lens//2 - 1) + self.kthSmallest(nums1, nums2, lens//2) ) / 2.0
        
    def kthSmallest(self, nums1, nums2, k):
        if not nums1:
            return nums2[k]
        if not nums2:
            return nums1[k]
        
        midIdx1, midIdx2 = len(nums1)//2, len(nums2)//2
        
        # when k is relatively large, then we can safely drop the first half that are surely smaller than the kth
        # the question is where is the first half that are surely smaller than the kth?
        # by comparing midVal1 and midVal2, we can find it out
        # if midVal1 < midVal2, then all the vals in nums1[:midIdx1] are less than midVal2 
        # also all of those vals are less than kth, we can safely drop all those vals
        if k > midIdx1 + midIdx2:
            if nums1[midIdx1] < nums2[midIdx2]:
                return self.kthSmallest(nums1[midIdx1 + 1:], nums2, k - midIdx1 - 1)
            else:
                return self.kthSmallest(nums1, nums2[midIdx2 + 1:], k - midIdx2 - 1)
            
        # when k is relatively small, then we can safely drop the second half that are surely larger than the kth
        # the question is where is the second half that are surely larger then the kth?
        # by comparing midVal1 and midVal2, we can find it out
        # if midVal1 > midVal2, then all the vals in nums1[midIdx1:] are larger than midVal2
        # also all of those vals are larger than kth, we can safely drop all those vals
        else:
            if nums1[midIdx1] > nums2[midIdx2]:
                return self.kthSmallest(nums1[:midIdx1], nums2, k)
            else:
                return self.kthSmallest(nums1, nums2[:midIdx2], k)

/********************************************java version***************************************/

class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int n = nums1.length + nums2.length;
        if (n % 2 == 0) {
            return (
                    findKth(nums1, 0, nums2, 0, n / 2) + 
                    findKth(nums1, 0, nums2, 0, n / 2 + 1)
                   ) / 2.0;
        } 
        return findKth(nums1, 0, nums2, 0, n / 2 + 1);
    }
    
    
    //在2个排序数组中寻找第K个数，K不是数组下标
    private int findKth(int[] nums1, int start1, 
                        int[] nums2, int start2, 
                        int k) {
        if (start1 >= nums1.length) {
            return nums2[start2 + k -1];
        }
        if (start2 >= nums2.length) {
            return nums1[start1 + k - 1];
        }
        
        if (k == 1) {
            return Math.min(nums1[start1], nums2[start2]);
        }
        
        //如果数组nums1已经不够K/2, 扔掉nums2前K/2, haltKthOf1 = Integer.MAX_VALUE;
        int haltKthOf1 = (start1 + k / 2 -1 < nums1.length) ? nums1[start1 + k / 2 - 1] : Integer.MAX_VALUE;

        //如果数组nums2已经不够K/2, 扔掉nums1前K/2, haltKthOf2 = Integer.MAX_VALUE;
        int haltKthOf2 = (start2 + k / 2 - 1< nums2.length) ? nums2[start2 + k / 2 - 1] : Integer.MAX_VALUE;
        
        if (haltKthOf1 < haltKthOf2) {
            return findKth(nums1, start1 + k / 2, nums2, start2, k - k / 2);
        } else {
            return findKth(nums1, start1, nums2, start2 + k / 2, k - k / 2);
        }
    } 
    
}

