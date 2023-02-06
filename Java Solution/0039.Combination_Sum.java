// backtrack
//https://leetcode.com/problems/combination-sum/solutions/16502/a-general-approach-to-backtracking-questions-in-java-subsets-permutations-combination-sum-palindrome-partitioning/
//总结的非常好

class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> res = new ArrayList<>();
        Arrays.sort(candidates);
        backtrack(res, new ArrayList<>(), candidates, target, 0);
        return res;
    }

    private void backtrack(List<List<Integer>> res, List<Integer> tempList, int [] nums, int remain, int start) {
        if (remain < 0) return;

        if (remain == 0) {
            res.add(new ArrayList<>(tempList));
            return;
        }
        
        for (int i = start; i < nums.length; i++) {
            tempList.add(nums[i]);
            backtrack(res, tempList, nums, remain - nums[i], i);
            tempList.remove(tempList.size() - 1);
        }

    }
}
