/*
Given an integer array nums, return the length of the longest strictly increasing subsequence.

A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements. For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].

 

Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Example 2:

Input: nums = [0,1,0,3,2,3]
Output: 4
Example 3:

Input: nums = [7,7,7,7,7,7,7]
Output: 1

*/

//version1: python

"""
1.状态定义：dp[i]以i结尾的最长子序列
2.求：dp[i]最大值
3.初始化：dp[0] = 1
4.递推公式：dp[i] = max(dp[j]+1) for j < i && nums[j] < nums[i];
O(N2) O(N)
"""
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
 
// follow up : print the path
when use which one element, pi[n] record the element index
then print

"""NlogN的算法，还是网上的高人讲得好。https://www.youtube.com/watch?v=YoeWZ3ELMEk"""
//version2: python
"""
dp是后退，nlogn选择正推
1.状态定义：dp[i]以i结尾的最长子序列
2.求：dp[i]最大值
3.初始化：dp[0] = 1
4.递推公式：dp[i] = max(dp[j]+1) for j < i && nums[j] < nums[i];
"""
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        size = 0
        
        for num in nums:
            #[40, 60] 10 [10, 60] 20 left side < 20
        
            i = bisect.bisect_left(dp, num, 0, size)  #0, 2 val < dp[i]   #i返回的是左边都比index小
            dp[i] = num
            if i == size: # 4,5,6
                size += 1
            
        return size
             
             
//version3: java
//1.定义dp[i] 代表严格以i结尾的最长子序列的长度
//2.求dp[i]最大值
//3.初始化dp[0] = 1;
//4.递推公式 dp[i] = max(dp[j]+1) for j < i && nums[j] < nums[i];
class Solution {
    public int lengthOfLIS(int[] nums) {
        //子序列和子数组
        int n = nums.length;
        int dp[] = new int[n];
        for (int i = 0; i < n; i++) {
            dp[i] = 1;
        }
                
        for (int i = 1; i < n; i++) {
            for (int j = i - 1; j >= 0; j--) {
                if (nums[j] < nums[i]) {
                    dp[i] = Math.max(dp[i], dp[j] + 1);
                }
            }
        }
        
        int maxLen = dp[0];
        for (int i = 0; i < n; i++) {
            maxLen = Math.max(maxLen, dp[i]);
        }
        return maxLen;
    }
}
