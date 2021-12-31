/*
Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

Example 1:

Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]
Example 2:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
*/

class Solution {
    public List<List<Integer>> permuteUnique(int[] nums) {
        List<List<Integer>> results = new ArrayList<>();
        if (nums == null || nums.length == 0) {
            return results;
        }
        Arrays.sort(nums);
        help(nums, new boolean[nums.length], new ArrayList<Integer>(), results);
        return results;        
    }
    
    private void help(int[] nums, boolean[] visited, List<Integer> permutation, List<List<Integer>> results) {
        if (permutation.size() == nums.length) {
            results.add(new ArrayList<Integer>(permutation));
            return;
        }
        
        for (int i = 0; i < nums.length; i++) {
            //如果已经加入了permutation就跳过
            if (visited[i]) {
                continue;
            }
            //连续相等的元素要按照顺序选择，不能跳着选
            if (i > 0 && (!visited[i-1]) && (nums[i] == nums[i-1])) {
                continue;
            }
            permutation.add(nums[i]);
            visited[i] = true;
            help(nums, visited, permutation, results);
            permutation.remove(permutation.size() - 1);
            visited[i] = false;
        }
    }
    
}



