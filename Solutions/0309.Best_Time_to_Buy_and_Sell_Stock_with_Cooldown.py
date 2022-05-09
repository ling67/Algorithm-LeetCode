You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:

After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

 

Example 1:

Input: prices = [1,2,3,0,2]
Output: 3
Explanation: transactions = [buy, sell, cooldown, buy, sell]
Example 2:

Input: prices = [1]
Output: 0
 

Constraints:

1 <= prices.length <= 5000
0 <= prices[i] <= 1000


"""
has to rest for one day before buy another stock
在不在手区分：今天交易完后有没有股票在手上：卖出是不在手，买入是在手
分两个状态：hold and unhold:
hold[i]=第i天又股票在手状态下的最大收益
unhold[i]=第i天没有股票在手状态下的最大收益 
递推公式 hold[i]
递推公式 unhold[i]
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        
        hold = [float("-inf") for _ in range(len(prices))]
        unhold = [float("-inf") for _ in range(len(prices))]
        hold[0] = -prices[0]   #第0天买入，后收益
        unhold[0] = 0   #第0天买入后收益
        hold[1] = max(-prices[0], -prices[1])
        unhold[1] = max(0, prices[1] - prices[0])
        
        for i in range(2, len(prices)):
            hold[i] = max(hold[i-1], unhold[i-2] - prices[i])  #今天买 或者 有股票
            unhold[i] = max(prices[i] + hold[i-1], unhold[i-1])  #今天卖 或者 没有股票
        
        return unhold[-1]
