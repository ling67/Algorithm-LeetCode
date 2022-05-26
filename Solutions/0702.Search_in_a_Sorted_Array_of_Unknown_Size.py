/*
This is an interactive problem.

You have a sorted array of unique elements and an unknown size. You do not have an access to the array but you can use the ArrayReader interface to access it. You can call ArrayReader.get(i) that:

returns the value at the ith index (0-indexed) of the secret array (i.e., secret[i]), or
returns 231 - 1 if the i is out of the boundary of the array.
You are also given an integer target.

Return the index k of the hidden array where secret[k] == target or return -1 otherwise.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: secret = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in secret and its index is 4.
Example 2:

Input: secret = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in secret so return -1.
 

Constraints:

1 <= secret.length <= 104
-104 <= secret[i], target <= 104
secret is sorted in a strictly increasing order.
*/

/**
 * // This is ArrayReader's API interface.
 * // You should not implement it, or speculate about its implementation
 * interface ArrayReader {
 *     public int get(int index) {}
 * }
 */


 # """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader: 'ArrayReader', target: int) -> int:
        start, end = 0, self._get_max_size(reader, target)
        while start + 1 < end:
            mid = start + (end - start) // 2
            if reader.get(mid) == target:
                return mid
            elif reader.get(mid) > target:
                end = mid
            else:
                start = mid
        if reader.get(start) == target:
            return start
        if reader.get(end) == target:
            return end
        return -1
        
    def _get_max_size(self, reader, target):
        end = 1
        while reader.get(end) < target:
            end *= 2
        return end
    
 
/*
I think we can use binary search, but the main point is we can not make sure end of array
1. we need to find the right border where the target located.
2. then we can use binary search to solve this problem
3. compare the target with the nums[mid], which is from start to end
4. if == return mid index
5. if larger, we search target in right side
6. otherwise, we search in left side
*/

class Solution {
    public int search(ArrayReader reader, int target) {
        
        if(reader.get(0) == target) {
            return 0;
        }
        
        int i = 1;
        while (reader.get(i) < target) {
            i = 2*i;
        }
        
        int start = 0, end = i;
        
        while (start + 1 < end) {
            int mid = start + (end-start)/2;
            if(reader.get(mid) == target) {
                return mid;
            } else if (reader.get(mid) < target) {
                start = mid;
            } else {
                end = mid;
            }
        }
        
        if (reader.get(start) == target) {
            return start;
        }
        if (reader.get(end) == target) {
            return end;
        }
        
        return -1;
        
    }
}
