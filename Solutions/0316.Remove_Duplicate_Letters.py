"""
Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

 

Example 1:

Input: s = "bcabc"
Output: "abc"
Example 2:

Input: s = "cbacdcbc"
Output: "acdb"
 

Constraints:

1 <= s.length <= 104
s consists of lowercase English letters.
"""

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        ch_last = defaultdict(int)
        for i in range (len(s)):
            ch_last[s[i]] = i
            
        included = set()
        st = []  #单调递增栈
        
        for i in range(len(s)):
            
            #ch要不要入栈，要看ch是不是已经在set中了
            if s[i] in included:
                continue
            
            #如果ch小于栈顶元素，要不要pop出栈顶元素要看，栈顶元素是不是最后一个重复元素的下标
            while len(st) > 0 and s[i] < st[-1] and ch_last[st[-1]] > i:  #如果不是最后一个，就可以删除，因为后面还有嘛
                val = st.pop()
                included.remove(val)
                    
            st.append(s[i])
            included.add(s[i])
        
        return "".join(st)
