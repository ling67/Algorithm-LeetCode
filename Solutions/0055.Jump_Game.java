/*
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

 

Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.

*/

"""
1.确定状态dp[j] 能不能跳到j
2.求dp[n-1]
3.初始化：dp[0] = true
4.递推公式 dp[j] = (0<i<j) i + a[i] > i
"""O(N^2), O(N)"""
"""
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [False] * len(nums)    # 确定状态：dp[j]表示能不能跳到位置j
        dp[0] = True                # 初始条件
        for j in range(1, len(nums)):
            for i in range(j):
                if dp[i] and i + nums[i] >= j:  # 转移方程：只要在dp[j]之前存在一个dp[i]=True且从这个i位置够得着j位置，那么dp[j]就为True
                    dp[j] = True
                    break
        
        return dp[-1]


/*
1.definition dp[i] represents the result of whether it is possible to skip from index 0 to the index i position
2.we require dp[n-1]
3.initialisation initialize dp, dp[0] = true 
4.recursion formular for each dp[j] j from 0 to i-1  if dp[j] == true && j + nums[j] >= i, we think dp[i] = true
*/
class Solution {
    public boolean canJump(int[] nums) {
        int n = nums.length;
        boolean[] dp = new boolean[n];
        Arrays.fill(dp, false);
        dp[0] = true;
        
        for (int i = 1; i < n; i++) {
            for (int j = 0; j < i; j++) {
                if (dp[j] && (j + nums[j] >= i)) {
                    dp[i] = true;
                    break;
                }
            }
        }
        return dp[n-1];
    }
}
