/*
Description
Given a string of char array and an offset, rotate the string by offset in place. (from left to right).
In different languages, str will be given in different ways. For example, the string "abc" will be given in following ways:

Java: char[] str = {'a', 'b', 'c'};
Python：str = ['a', 'b', 'c']
C++：string str = "abc";
Wechat reply the 【8】 get the latest frequent Interview questions . (wechat id : jiuzhang15)

offset >= 0
the length of str >= 0
In place means you should change strings in the function. You don't return anything.

Example
Example 1:

Input:

str = ""abcdefg"
offset = 3
Output:

"efgabcd"
Explanation:

Note that it is rotated in place, that is, after str is rotated, it becomes "efgabcd".

Example 2:

Input:

str = ""abcdefg"
offset = 0
Output:

"abcdefg"
Explanation:

Note that it is rotated in place, that is, after str is rotated, it becomes "abcdefg".

Example 3:

Input:

str = ""abcdefg"
offset = 1
Output:

"gabcdef"
Explanation:

Note that it is rotated in place, that is, after str is rotated, it becomes "gabcdef".

Example 4:

Input:

str = ""abcdefg"
offset = 2
Output:

"fgabcde"
Explanation:

Note that it is rotated in place, that is, after str is rotated, it becomes "fgabcde".

Example 5:

Input:

str = ""abcdefg"
offset = 10
Output:

"efgabcd"
Explanation:

Note that it is rotated in place, that is, after str is rotated, it becomes "efgabcd".
*/

public class Solution {
    /**
     * @param str: An array of char
     * @param offset: An integer
     * @return: nothing
     */
    public void rotateString(char[] str, int offset) {
        // write your code here
        if (str == null || str.length == 0) {
            return;
        }

        offset = offset % str.length;
        reverse(str, 0, str.length - offset - 1);
        reverse(str, str.length - offset, str.length - 1);
        reverse(str, 0, str.length - 1);
    }

    private void reverse(char[] str, int start, int end) {
        for (int i = start, j = end; i < j; i++, j--) {
            char temp = str[i];
            str[i] = str[j];
            str[j] = temp;
        }
    }
}
