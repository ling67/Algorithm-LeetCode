/*
Description
Give you an integer array (index from 0 to n-1, where n is the size of this array, value from 0 to 10000) and an query list. For each query, give you an integer, return the number of elements in the array that are smaller than the given integer.

Wechat reply 【248】 get the latest requent Interview questions . (wechat id : jiuzhang15)

We suggest you finish problem Segment Tree Buildand Segment Tree Query II first.

Example
Example 1:

Input: array =[1,2,7,8,5] queries =[1,8,5]
Output:[0,4,2]
Example 2:

Input: array =[3,4,5,8] queries =[2,4]
Output:[0,1]
Challenge
Could you use three ways to do it.

Just loop
Sort and binary search
Build Segment Tree and Search.

*/

public class Solution {
    /**
     * @param A: An integer array
     * @param queries: The query list
     * @return: The number of element in the array that are smaller that the given integer
     */
    public List<Integer> countOfSmallerNumber(int[] A, int[] queries) {
        // write your code here
        List<Integer> nums = new ArrayList<>();
        if (A == null || A.length == 0) {
            for (int i = 0; i < queries.length; i++) {
                nums.add(0);
            } 
            return nums;
        }
        
        Arrays.sort(A);
        for (int i = 0; i < queries.length; i++) {
            nums.add(firstLarger(A, queries[i]));
        }
        return nums;
    }

    // find the first index equal or larger than the value
    private int firstLarger(int[] A, int num) {
        int start = 0, end = A.length;
        while (start + 1 < end) {
            int mid = start + (end - start) / 2;
            if (A[mid] == num) {
                end = mid;
            } else if (A[mid] < num) {
                start = mid;
            } else {
                end = mid;
            }
        }
        if(A[start] >= num) {
            return start;
        }
        return end;
    }
}


