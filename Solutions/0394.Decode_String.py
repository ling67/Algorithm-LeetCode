"""
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

 

Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"
Example 2:

Input: s = "3[a2[c]]"
Output: "accaccacc"
Example 3:

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
 

Constraints:

1 <= s.length <= 30
s consists of lowercase English letters, digits, and square brackets '[]'.
s is guaranteed to be a valid input.
All the integers in s are in the range [1, 300].
"""
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for ch in s:
            if ch == ']':
                strs = []
                while stack and stack[-1] != '[':
                    strs.append(stack.pop())
                    
                stack.pop()
                
                repeats = 0
                base = 1
                while stack and stack[-1].isdigit():
                    repeats += (ord(stack.pop()) - ord('0')) * base
                    base *= 10
                stack.append(''.join(reversed(strs)) * repeats)
            else:
                stack.append(ch)
        return ''.join(stack)
       
class Solution:
    def decodeString(self, s: str) -> str:
        nums_st = []    #staore num in s
        ch_st = [""]
        i = 0
        while i < len(s):
            ch = s[i]
            if ch.isdigit():
                num = ord(ch) - ord("0")
                while i + 1 < len(s) and s[i+1].isdigit():   #应对25[b]这种情况
                    num = 10 * num + ord(s[i+1]) - ord("0")
                    i += 1
                nums_st.append(num)
                
            elif ch.isalpha():
                ch_st[-1] += ch   # 注意不能用ch_st.append(ch)，不然"3[a2[c]]"中a和cc就分开了
            
            elif ch == "[":
                ch_st.append("")  # 注意这里append空ch
            
            elif ch == "]":
                top_num = nums_st.pop()
                top_ch = ch_st.pop()
                ch_st[-1] += top_num * top_ch   
            i += 1
        
        return ch_st[0]
