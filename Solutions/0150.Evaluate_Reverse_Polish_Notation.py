"""
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, and /. Each operand may be an integer or another expression.

Note that division between two integers should truncate toward zero.

It is guaranteed that the given RPN expression is always valid. That means the expression would always evaluate to a result, and there will not be any division by zero operation.

 

Example 1:

Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
Example 2:

Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6
Example 3:

Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
 

Constraints:

1 <= tokens.length <= 104
tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the range [-200, 200].
"""

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        num_st = []
        for ch in tokens:
            if ch == "+":
                num_st.append(num_st.pop() + num_st.pop())
            elif ch == "-":
                num_st.append(- num_st.pop() + num_st.pop())  #容易错，这里是倒序
            elif ch == "*":
                num_st.append(num_st.pop() * num_st.pop())
            elif ch == "/":
                #Note that division between two integers should truncate toward zero. 6//8 = 0, but 6//(-8) = -1, so we use int()
                num_st.append(int(1 / num_st.pop() * num_st.pop()))  
            else:
                num_st.append(int(ch))
        return num_st[-1]

