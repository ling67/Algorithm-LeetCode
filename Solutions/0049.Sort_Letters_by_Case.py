"""
Description
Given a string chars which contains only letters. Sort it by lower case first and upper case second.
In different languages, chars will be given in different ways. For example, the string "abc" will be given in following ways:

Java: char[] chars = {'a', 'b', 'c'};
Python：chars = ['a', 'b', 'c']
C++：string chars = "abc";
You need to use an in-place algorithm to solve this problem.

Wechat reply the 【49】 get the latest frequent Interview questions . (wechat id : jiuzhang15)

It's NOT necessary to keep the original order of lower-case letters and upper case letters.

Example
Example 1:

Input:

chars = "abAcD"
Output:

"acbAD"
Explanation:

You can also return "abcAD" or "cbaAD" or other correct answers.
Example 2:

Input:

chars = "ABC"
Output:

"ABC"
Explanation:

You can also return "CBA" or "BCA" or other correct answers.

Challenge
Do it in one-pass and in-place.
"""

from typing import (
    List,
)

class Solution:
    """
    @param chars: The letter array you should sort by Case
    @return: nothing
    """
    def sortLetters(self, chars: List[str]):
        # write your code here
        i, j = 0, len(chars) - 1

        while i < j:
            while i < j and chars[i] >= 'a' and chars[j] <= 'z':
                i += 1
            while i < j and chars[j] >= 'A' and chars[j] <= 'Z':
                j -= 1

            if i < j:
                temp = chars[i]
                chars[i] = chars[j]
                chars[j] = temp
                i += 1
                j -= 1
        return chars

