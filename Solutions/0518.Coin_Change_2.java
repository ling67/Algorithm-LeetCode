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
