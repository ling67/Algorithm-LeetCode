//Solution: Expand Around Center  
//In fact, we could solve it in O(n^2) time using only constant space.

class Solution {
    public String longestPalindrome(String s) {
        if (s == null || s.length() < 1) return "";
        int start = 0, end = 0;
        for (int i = 0; i < s.length(); i++) {
            int len1 = expandAroundCenter(s, i, i);
            int len2 = expandAroundCenter(s, i, i + 1);
            int len = Math.max(len1, len2);
            if (len > end - start) {
                start = i - (len - 1) / 2;
                end = i + len / 2;
            }
        }
        return s.substring(start, end + 1);
    }

    private int expandAroundCenter(String s, int left, int right) {
        int l = left, r = right;
        while (l >= 0 && r < s.length() && s.charAt(l) == s.charAt(r)) {
            l--;
            r++;
        }
        return r - l - 1;
    }
}

//dp solution
Close
happy_little_pig
happy_little_pig
Feb 20, 2023 22:06

Details
Solution
Java
Runtime
254 ms
Beats
23.7%
Memory
45.6 MB
Beats
22.99%
Click the distribution chart to view more details
Notes
Write your notes here
Related Tags
Select tags
0/5
/*
dp[i][j] 代表s[i...j]是不是一个回文串
dp[i][j] = True if dp[i+1][j-1] is true and s[i] = s[j] or j-i == 1
return the longest substring for all dp[i][j] = True
 */
class Solution {
    public String longestPalindrome(String s) {
        if (s == null || s.length() == 0) return "";

        int n = s.length();
        boolean[][] dp = new boolean[n][n];

        for (int i = 0; i < n; i++) {
            dp[i][i] = true;
        }

        for (int i = n - 1; i > -1; i--) {
            for (int j = i + 1; j < n; j++) {
                if (s.charAt(i) == s.charAt(j) && (j - i == 1 || dp[i + 1][j - 1])) {
                    dp[i][j] = true;
                }
            }
        }

        int maxLen = 1;
        String res = s.substring(0, 1);
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if (dp[i][j] && maxLen < j - i + 1) {
                    maxLen = j - i + 1;
                    res = s.substring(i, j + 1);
                }
            }
        }
        return res.toString();
    }
}
