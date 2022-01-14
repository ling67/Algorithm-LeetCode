/*
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
 

Example 1:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
Example 2:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
*/

/*
method 1.row = index // n and col = idx % n;
method 2.先竖向搜索确定行，再横向收索确定列
*/
class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int m = matrix.length;
        if (m == 0) {
            return false;
        }
        int n = matrix[0].length;
        
        //binary search
        int start = 0, end = m * n - 1;
        while (start + 1 < end) {
            int pivotIdx = start + (end - start) / 2;
            int pivotElement = matrix[pivotIdx / n][pivotIdx % n];
            if (target == pivotElement) {
                return true;
            } else if (target > pivotElement) {
                start = pivotIdx;
            } else {
                end = pivotIdx;
            }
        }
        
        int startValue = matrix[start / n][start % n];
        int endValue = matrix[end / n][end % n];
        
        return (startValue == target || endValue == target) ? true : false;      
    }
}
