// compare the size of hashmap and length of array
class Solution {
    public boolean containsDuplicate(int[] nums) {
        int len = nums.length;
        Map<Integer, Integer> map = new HashMap<>();
        for (int num:nums) {
            map.put(num, map.getOrDefault(num, 0) + 1);
        }
        if (map.size() == len) {
            return false;
        } else {
            return true;
        }
    }
}
