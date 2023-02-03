//method 1: sort then return the middle element
class Solution {
    public int majorityElement(int[] nums) {
        Arrays.sort(nums);
        int n = nums.length;
        return nums[n/2];
    }
}

//method 2: hashmap record the feq of the element
class Solution {
    public int majorityElement(int[] nums) {
        int len = nums.length;
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < len; i++) {
             map.put(nums[i], map.getOrDefault(nums[i], 0) + 1);
        }

        for (int num : nums) {
            if (map.get(num) > len / 2) {
                return num;
            }
        }
        return 0;
    }
}
