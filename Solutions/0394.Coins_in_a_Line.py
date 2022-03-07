"""
Solution1 dp: f[i]=面对i个石子，先手是必胜吗; f[i]=True if f[i-1] or f[i-2] 有一个是False
Solution 2: 至于prev, curr有关，所以可以空间优化成O(1)了; 
Solution 3 数学: 只要是3的倍数就一定输 return n % 3 != 0
"""

"""
设f[i]表示面对i个石子，是否先手必胜(f[i] = TRUE / FALSE)
 
f[i] =
TRUE，f[i-1]==FALSE AND f[i-2]==FALSE 拿1或2个石子都必胜
TRUE，f[i-1]==FALSE AND f[i-2]==TRUE 拿1个石子必胜
TRUE，f[i-1]==TRUE AND f[i-2]==FALSE 拿2个石子必胜
FALSE，f[i-1]==TRUE AND f[i-2]==TRUE 必败

f[i] = f[i-1] == FALSE OR f[i-2] == FALSE
"""

class Solution:
    """
    @param n: An integer
    @return: A boolean which equals to true if the first player will win
    """
    def firstWillWin(self, n):
        if n == 0:
            return False
            
        if n <= 2:
            return True
            
        dp = [True] * (n + 1)
        dp[0] = dp[1] = dp[2] = True
        
        for i in range(3, n + 1):
            if not dp[i - 1] or not dp[i - 2]:
                dp[i] = True
                
            else:
                dp[i] = False
                
        return dp[n]
      
Solution 2: 空间优化
class Solution:
    def firstWillWin(self, n):
        if n == 0:
            return False
        if n == 1 or n == 2:
            return True
            
        prev, curr = True, True    #prev记录dp[i-2] curr记录dp[i-1]
        
        for i in range(3, n + 1):
            tempCurr = curr
            if not prev or not curr:
                curr = True
                prev = tempCurr
            else:
                curr = False
                prev = tempCurr
                
        return curr
      
Solution 3: 数学规律法
class Solution:
    def firstWillWin(self, n):
        return n % 3 != 0
