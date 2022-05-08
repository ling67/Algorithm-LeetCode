/*
Given an array of non-negative integers nums, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

You can assume that you can always reach the last index.

 

Example 1:

Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [2,3,0,1,4]
Output: 2
*/

"""
 Python
1.define state: dp[i] the minimum number of jumps
2.get dp[n-1]
3.dp[0] = 0 dp[1] = 1
4.transit function dp[j] = min{dp[i] + 1} 0 < i < j  if i + nums[i] >= j
"""
class Solution:
    def jump(self, nums: List[int]) -> int:
        
        n = len(nums)
        if n == 1:
            return 0
        
        dp = [float('inf')] * n   
        dp[0] = 0
        dp[1] = 1
        
        for i in range(2, n):
            for j in range(i):
                if j + nums[j] >= i:
                    dp[i] = min(dp[i], dp[j] + 1)
        return dp[n-1]
        

/*
1.definition dp[i] represent the minimum number of jumps to reach the i index 
2.we require dp[n-1]
3.initialization initialize the dp[0] = 0
4.recursion fomular dp[i] = min(d[j] + 1) each j from 0 to i-1 && A[j] >= i-j
*/
class Solution {
    public int jump(int[] nums) {
        int n = nums.length;
        int[] dp = new int[n];
        Arrays.fill(dp, Integer.MAX_VALUE);
        dp[0] = 0;
        for (int i = 1; i < n; i++) {
            for (int j = 0; j < i; j++) {
                if (nums[j] >= i - j) {
                    dp[i] = Math.min(dp[i], dp[j] + 1);
                }
            }
        }
        return dp[n-1];
    }
}
