/*
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Example 2:

Input: nums = []
Output: []
Example 3:

Input: nums = [0]
Output: []

*/

class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> results = new ArrayList<>();
        if (nums == null || nums.length < 3) {
            return results;
        }
        Arrays.sort(nums);
        for (int i = 0; i < nums.length - 2; i++) {
            //固定数组一端的端点，端点可能有重复
            if (i > 0 && nums[i] == nums[i - 1]) {
                continue;
            }
            int left = i + 1, right = nums.length - 1;
            int target = -nums[i]; 
            twoSum(nums, left, right, target, results);
        }
        return results;
    }
    
    private void twoSum(int[] nums, 
                        int left, 
                        int right, 
                        int target, 
                        List<List<Integer>> results) {
        while (left < right) {
            if(nums[left] + nums[right] == target) {
                ArrayList<Integer> triple = new ArrayList<>();
                triple.add(-target);
                triple.add(nums[left]);
                triple.add(nums[right]);
                results.add(triple);
                left++;
                right--;
                
                //只有等于的时候处理，去除左边重复元素
                while (left < right && nums[left] == nums[left - 1]) {
                    left++;
                }
                //只有等于的时候处理，去除右边重复元素
                while (left < right && nums[right] == nums[right + 1]) {
                    right--;
                }
            } else if (nums[left] + nums[right] <target) {
                left++;
            } else {
                right--;
            }
        }
    }
}

