/*
Given an integer n, return the least number of perfect square numbers that sum to n.

A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.

 

Example 1:

Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.

*/

/*
I think this problem we can use danymic programming to solve it.
step 1.define dp array, dp[i] represent the least number of perfect square number that sum to i.
step 2.the result we require is dp[n]
step 3.Initialization，initialize dp dp[0] = 0. dp[1] = 1. dp[2] = 2, dp[3] = 3 dp[4] = 1;
step 4.we need to find the recurrence formula  dp[i] = min(dp[i - j * j] + 1) for j from 0 to the square of j < i

good explainer video : https://www.youtube.com/watch?v=HLZLwjzIVGo
*/
class Solution {
    public int numSquares(int n) {
        //create a new array  
        //initialize the array
        int dp[] = new int[n+1];
        Arrays.fill(dp, Integer.MAX_VALUE);  //pay attention do not forget initialize the array
        dp[0] = 0;
        for (int i = 1; i < n + 1; i++) {
            for (int j = 1; j * j <= i; j++) {
                dp[i] = Math.min(dp[i], dp[i-j*j] + 1);
            }
        }
        return dp[n];
    }
}

