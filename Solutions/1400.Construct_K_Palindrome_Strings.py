"""
Given a string s and an integer k, return true if you can use all the characters in s to construct k palindrome strings or false otherwise.

 

Example 1:

Input: s = "annabelle", k = 2
Output: true
Explanation: You can construct two palindromes using all characters in s.
Some possible constructions "anna" + "elble", "anbna" + "elle", "anellena" + "b"
Example 2:

Input: s = "leetcode", k = 3
Output: false
Explanation: It is impossible to construct 3 palindromes using all the characters of s.
Example 3:

Input: s = "true", k = 4
Output: true
Explanation: The only possible solution is to put each character in a separate string.
 

Constraints:

1 <= s.length <= 105
s consists of lowercase English letters.
1 <= k <= 105

"""

//讲解：https://leetcode-cn.com/problems/construct-k-palindrome-strings/solution/gou-zao-k-ge-hui-wen-zi-fu-chuan-by-leetcode-solut/
 
class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        # 右边界为字符串的长度
        right = len(s)
        # 统计每个字符出现的次数
        occ = collections.Counter(s)
        # 左边界为出现奇数次字符的个数
        left = sum(1 for _, v in occ.items() if v % 2 == 1)
        left = max(left, 1)
        return left <= k <= right

#从可迭代对象中实例化 Counter
#b = Counter("chenkc") # string

class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False
        center = Counter(s)     #是dict子类
        odd_cnt = 0
        for cnt in center.values():
            if cnt % 2 == 1:
                odd_cnt += 1
            if odd_cnt > k:
                return False
            
        return True
        
