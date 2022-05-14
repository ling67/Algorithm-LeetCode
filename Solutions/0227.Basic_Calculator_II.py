"""
Given a string s which represents an expression, evaluate this expression and return its value. 

The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

 

Example 1:

Input: s = "3+2*2"
Output: 7
Example 2:

Input: s = " 3/2 "
Output: 1
Example 3:

Input: s = " 3+5 / 2 "
Output: 5
 

Constraints:

1 <= s.length <= 3 * 105
s consists of integers and operators ('+', '-', '*', '/') separated by some number of spaces.
s represents a valid expression.
All the integers in the expression are non-negative integers in the range [0, 231 - 1].
The answer is guaranteed to fit in a 32-bit integer.
"""

class Solution:
    def calculate(self, s: str) -> int:
        num_stack = []
        operator_stack = []
        
        #删除string中所有" "
        new_str = ""
        for ch in s:
            if ch != " ":
                new_str += ch
                
        s = new_str
        n = len(new_str)
        i = 0
        
        while i < n:
            
            #如果是数字要往后找到所有数字，例如：123
            if s[i].isdigit():
                val = 0
                while i < n and s[i].isdigit():
                    val = val *10 + int(s[i])
                    i += 1
                num_stack.append(val)
            
            #如果是乘法或者除法，找到后面的数字直接跟num_stack中数字先做运算
            if i < n and s[i] == '*':
                if s[i+1].isdigit():
                    val = 0
                    while i+1 < n and s[i+1].isdigit():
                        val = val*10 + int(s[i+1])
                        i += 1
                num_stack[-1] *= val
            
            if i < n and s[i] == '/':
                if s[i+1].isdigit():
                    val = 0
                    while i+1 < n and s[i+1].isdigit():
                        val = val *10 + int(s[i+1])
                        i += 1
                num_stack[-1] //= val 

            #如果是加法或者减法，入栈
            if i < n and s[i] in ['+', '-']:
                operator_stack.append(s[i])
        
            i += 1
        
        #遍历剩下来的栈，然后做加减法
        res = num_stack[0]  
        for i in range(len(operator_stack)):
            if operator_stack[i] == '+':
                res += num_stack[i+1]  #注意要用res
            if operator_stack[i] == '-':
                res -= num_stack[i+1]
                
        return res
        
