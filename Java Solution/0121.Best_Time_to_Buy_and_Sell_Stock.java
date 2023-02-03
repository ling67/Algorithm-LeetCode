
class Solution {
    public int maxProfit(int[] prices) {
        int minValue = prices[0];
        int maxProfit = Integer.MIN_VALUE;
        for (int i = 0; i < prices.length; i++) {
            int diff = prices[i] - minValue;
            maxProfit = Math.max(maxProfit, diff);
            minValue = Math.min(minValue, prices[i]);
        }
        return maxProfit;
    }
}
