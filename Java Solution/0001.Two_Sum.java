//method 1: brute force

class Solution {
    public int[] twoSum(int[] nums, int target) {
        int n = nums.length;
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if (nums[i] + nums[j] == target) {
                    return new int[] {i, j};
                }
            }
        }
        return null;
    }
}

//method 2: hashmap
class Solution {
    public int[] twoSum(int[] nums, int target) {
        int n = nums.length;
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < n; i++) {
            int remain = target - nums[i];
            if (map.containsKey(remain)) {
                return new int[] {map.get(remain), i};
            } else {
                map.put(nums[i], i);
            }
        }
        return null;
    }
}

//method 3: two point --- the index will change after you sort the array.



