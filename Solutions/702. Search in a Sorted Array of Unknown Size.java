/**
 * // This is ArrayReader's API interface.
 * // You should not implement it, or speculate about its implementation
 * interface ArrayReader {
 *     public int get(int index) {}
 * }
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
