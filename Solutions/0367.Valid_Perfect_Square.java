/*
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Follow up: Do not use any built-in library function such as sqrt.

 

Example 1:

Input: num = 16
Output: true
Example 2:

Input: num = 14
Output: false

*/

class Solution {
    public boolean isPerfectSquare(int num) {
        int start = 1, end = num;
        while (start + 1 < end) {
            int mid = start + (end - start) / 2;  // to avoid overflow incase (left+right)>2147483647
            int res = num / mid, remain = num % mid;
            if (res == mid && remain == 0) {  // check if mid * mid == num
                return true;
            } else if (res > mid) {   // mid is small -> go right to increase mid
                start = mid;
            } else {
                end = mid;     // mid is large -> to left to decrease mid
            }
        }
        if ((start * start == num) || (end * end == num)) {
            return true;
        }
        return false;
    }
}
