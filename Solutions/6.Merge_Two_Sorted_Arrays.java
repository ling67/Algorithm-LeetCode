"""
Description
Merge two given sorted ascending integer array A and B into a new sorted integer array.

Wechat reply 【6】 get the latest requent Interview questions . (wechat id : jiuzhang15)

Example
Example 1:

Input:

A = [1]
B = [1]
Output:

[1,1]
Explanation:

return array merged.

Example 2:

Input:

A = [1,2,3,4]
B = [2,4,5,6]
Output:

[1,2,2,3,4,4,5,6]
Challenge
How can you optimize your algorithm if one array is very large and the other is very small?

"""
class Solution {
    /**
     * @param A and B: sorted integer array A and B.
     * @return: A new sorted integer array
     */
    public int[] mergeSortedArray(int[] A, int[] B) {
        if (A == null || B == null) {
            return null;
        }
        
        int[] result = new int[A.length + B.length];
        int i = 0, j = 0, index = 0;
        
        while (i < A.length && j < B.length) {
            if (A[i] < B[j]) {
                result[index++] = A[i++];
            } else {
                result[index++] = B[j++];
            }
        }
        
        while (i < A.length) {
            result[index++] = A[i++];
        }
        while (j < B.length) {
            result[index++] = B[j++];
        }
        
        return result;
    }
}

//follow up
public class Solution {
    /*
     * @param A: sorted integer array A
     * @param B: sorted integer array B
     * @return: A new sorted integer array
     */
    public int[] mergeSortedArray(int[] A, int[] B) {
        if(A == null || A.length == 0) return B;
        if(B == null || B.length == 0) return A;
        int[] res = new int[A.length + B.length];
        int idx = 0;
        int pa = 0;
        for(int i=0;i<B.length;i++){
            int position = binarySearch(A, B[i]);
            while(pa < position){
                res[idx++] = A[pa++];
            }
            res[idx++] = B[i];
        }
        while(pa < A.length){
            res[idx++] = A[pa++];
        }
        return res;
    }
    
    private int binarySearch(int[] A, int target){
        int left = 0;
        int right = A.length-1;
        while(left <= right){
            int mid = left + (right-left)/2;
            if(A[mid] == target) return mid;
            if(target < A[mid]){
                right = mid - 1;
            }else{
                left = mid + 1;
            }
        }
        return left;
    }
}
