"""
Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

If multiple answers are possible, return any of them.

It is guaranteed that the length of the answer string is less than 104 for all the given inputs.

 

Example 1:

Input: numerator = 1, denominator = 2
Output: "0.5"
Example 2:

Input: numerator = 2, denominator = 1
Output: "2"
Example 3:

Input: numerator = 4, denominator = 333
Output: "0.(012)"
 

Constraints:

-231 <= numerator, denominator <= 231 - 1
denominator != 0
"""

class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        res = ""
        
        #handle divisible cases
        if numerator % denominator == 0:
            return str(numerator // denominator)
        
        #handle the result negtive cases
        if numerator / denominator < 0:
            res += '-'
        
        #handle integer part
        numerator = abs(numerator)
        denominator = abs(denominator)
        
        res += str(numerator // denominator)
        res += '.'
        
        #handle fractional parts
        remainder = numerator % denominator
        remain_to_pos = defaultdict(int)  #store remiander, pos
        curr_pos = 0
        decimal = ""
        
        while remainder != 0:
            #if reminder in mapping
            if remainder in remain_to_pos:
                reocurr_pos = remain_to_pos[remainder]
                decimal = decimal[:reocurr_pos] + '(' + decimal[reocurr_pos:] + ')'
                break
            
            #store the remainder
            remain_to_pos[remainder] = curr_pos
            curr_pos += 1
            
            #simulate division process
            remainder *= 10
            decimal += str(remainder // denominator)
            remainder %= denominator
            
        return res + decimal
