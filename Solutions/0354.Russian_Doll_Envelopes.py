"""
You are given a 2D array of integers envelopes where envelopes[i] = [wi, hi] represents the width and the height of an envelope.

One envelope can fit into another if and only if both the width and height of one envelope are greater than the other envelope's width and height.

Return the maximum number of envelopes you can Russian doll (i.e., put one inside the other).

Note: You cannot rotate an envelope.

 

Example 1:

Input: envelopes = [[5,4],[6,4],[6,7],[2,3]]
Output: 3
Explanation: The maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).
Example 2:

Input: envelopes = [[1,1],[1,1],[1,1]]
Output: 1
 

Constraints:

1 <= envelopes.length <= 105
envelopes[i].length == 2
1 <= wi, hi <= 105
"""

"""
python
1.define state dp[i] represent the max number of envelopes end with envelopes[i] 
2.get result dp[n-1]
3.initialize dp[0] = 1
4.transit function dp[i] = max{dp[j] + 1} 
envelopes[j][0]<envelopes[i][0]
envelopes[j][1]<envelopes[i][1]
O(nlogn + n2)  超时
"""
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], x[1]))
        
        n = len(envelopes)
        dp = [1] * n
        for i in range(1, n):
            for j in range(i):
                if envelopes[i][0] > envelopes[j][0] and envelopes[i][1] > envelopes[j][1]:
                    dp[i] = max(dp[i], 1+dp[j])
        return max(dp)
