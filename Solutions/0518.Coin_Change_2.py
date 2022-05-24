/*
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the number of combinations that make up that amount. If that amount of money cannot be made up by any combination of the coins, return 0.

You may assume that you have an infinite number of each kind of coin.

The answer is guaranteed to fit into a signed 32-bit integer.

 

Example 1:

Input: amount = 5, coins = [1,2,5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
Example 2:

Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.
Example 3:

Input: amount = 10, coins = [10]
Output: 1

*/

"""
1.定义状态dp[i] = how many ways get i
2.求dp[amount]
3.初始条件dp[0] = 1
4.递推公式 dp[i] = dp[i-coins[1]] + dp[i-coins[2]] +...
"""
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)         # dp[i] = how many ways get i
        dp[0] = 1
        
        # 这样写可以保证避开(1,3)和(3,1)的问题，因为当coin遍历到coin=1的时候，dp[4]+=d[3]此时的dp[3]=0所以dp[4]实际上加的是0
        # 而当coin遍历到coin=3的时候，dp[4]+=d[1]，此时d[1]被更新过一次。所以真个过程dp[4]只被更新一次，不会重复更新。
        for coin in coins:      
            for num in range(1, amount + 1):
                if num - coin >= 0:
                    dp[num] += dp[num - coin]

        return dp[amount]  
            
        
//version 1: dfs not work 超时
class Solution {
    public int change(int amount, int[] coins) {
        List<List<Integer>> result = new ArrayList<>();
        Arrays.sort(coins);
        help(coins, amount, 0, new ArrayList<>(), result);
        return result.size();
    }
    
    //得到所有的结果放入result中
    private void help(int[] coins,
                    int target,
                    int startIndex,
                    List<Integer> combination,
                    List<List<Integer>> result) {
        
        //exit
        if (target == 0) {
            result.add(new ArrayList<Integer>(combination));
        }
        
        //split
        for (int i = startIndex; i < coins.length; i++) {
            if (coins[i] > target) {
                return;
            }
            
            combination.add(coins[i]);
            help(coins, target - coins[i], i, combination, result);
            combination.remove(combination.size() - 1);
        }
        
    }
    
}
