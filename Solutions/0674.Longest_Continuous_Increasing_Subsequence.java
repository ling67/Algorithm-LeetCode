/*
Given an unsorted array of integers nums, return the length of the longest continuous increasing subsequence (i.e. subarray). The subsequence must be strictly increasing.

A continuous increasing subsequence is defined by two indices l and r (l < r) such that it is [nums[l], nums[l + 1], ..., nums[r - 1], nums[r]] and for each l <= i < r, nums[i] < nums[i + 1].

 

Example 1:

Input: nums = [1,3,5,4,7]
Output: 3
Explanation: The longest continuous increasing subsequence is [1,3,5] with length 3.
Even though [1,3,5,7] is an increasing subsequence, it is not continuous as elements 5 and 7 are separated by element
4.
Example 2:

Input: nums = [2,2,2,2,2]
Output: 1
Explanation: The longest continuous increasing subsequence is [2] with length 1. Note that it must be strictly
increasing.
*/


"""
1.dp[i]以i结尾的最长子序列长度
2.求dp[n-1]
3.初始条件：dp[0] = 1
4.dp[i] = max{1, dp[i-1] + 1(if nums[i] > nums[i-1])}
"""
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        
        dp[0] = 1
        
        for i in range(1, n):
            if nums[i] > nums[i-1]:
                dp[i] = dp[i-1] + 1
                
        res = 1
        for i in range(n):
            res = max(res, dp[i])
        
        return res
 

 """
version2： 空间优化             
1.确定状态 dp[i][j] 表示到坐标[i+1][j+1]的最小路径和
2.求 dp[m-1][n-1]
3.初始化 dp[0][0] = grid[0][0]
4.递推公式 dp[m-1][n-1] = grid[m-1][n-1] + min{dp[m-2][n-1], dp[m-1][n-2]}
O(m*n)

空间优化：由于dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
也就是说dp[i][j]只与他的前一行有关，所以计算得到了了dp[7]之后，就可以吧dp[6]之前都删掉了，因为再需要计算dp[8]的时候用不到，所以dp每次只需要保存一行数组用于后面的计算就可以了。如何实现呢？我们是用滚动数组：一开始不要开m行，之开两行dp[0][]和dp[1][]两行，初始化dp[0][]，计算dp[1][]，然后计算dp[2][]的时候就不需要dp[0][]了，把dp[2][]存到dp[0][]里面就可以了
空间就优化为O(N)了

"""
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(2)]
        
        #初始化
        dp[0][0] = grid[0][0]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[i][j] = grid[i][j]
                elif i == 0:
                    dp[i][j] = dp[i][j - 1] + grid[i][j]
                
                elif j == 0:
                    if i % 2 == 1:
                        dp[1][j] = dp[0][j] + grid[i][j]
                    else:
                        dp[0][j] = dp[1][j] + grid[i][j]   
                        
                else:
                    if i % 2 == 1:
                        dp[1][j] = min(dp[0][j], dp[1][j - 1]) + grid[i][j]
                    else:
                        dp[0][j] = min(dp[1][j], dp[0][j - 1]) + grid[i][j]                
                
        return dp[1][-1] if m % 2 == 0 else dp[0][-1]
        
        
        
        
/*
1.definition dp[i] represent the longest continuous increasing subsequence end with i
2.we require max(dp[j]) j from 0 to n-1
3.initialize the dp[i] = 1 each i from 0 to n-1
4.recursion fomular dp[i] = max(dp[i-1] + 1); nums[i] > nums[j] 
*/
class Solution {
    public int findLengthOfLCIS(int[] nums) {
        int n = nums.length;
        int[] dp = new int[n];
        Arrays.fill(dp, 1);
        for (int i = 1; i < n; i++) {
            if (nums[i-1] < nums[i]) {
                dp[i] = dp[i-1] + 1;
            }
        }
        
        int result = 1;
        for (int i = 0; i < n; i++) {
            result = (result >= dp[i] ? result : dp[i]);
        }
        return result;
    }
}
