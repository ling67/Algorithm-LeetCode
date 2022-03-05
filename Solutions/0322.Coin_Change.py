"""
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

 

Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Example 3:

Input: coins = [1], amount = 0
Output: 0
 

Constraints:

1 <= coins.length <= 12
1 <= coins[i] <= 231 - 1
0 <= amount <= 104
"""

"""
1.确定状态：dp[i] 和为i时最少需要多少硬币
2.返回dp[amount]
3.dp[0] = 0
4.dp[i] = min{min(dp[i-coins[0]]), min(dp[i-coins[1]]), min(dp[i-coins[n]]).....} +1
"""

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")] * (amount + 1) #dp[i]表示amount = i时最少的方法数
        dp[0] = 0;    #初始条件
        for num in range(1, amount + 1): #注意for循环里不要包含初始条件
            for coin in coins:
                if num - coin >= 0:   #这里判断是为了防止越界
                    dp[num] = min(dp[num - coin] + 1, dp[num])
                    
        return dp[-1] if dp[-1] != float("inf") else -1
            

