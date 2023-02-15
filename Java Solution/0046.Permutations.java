class Solution {
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        if (nums == null || nums.length == 0) return res;
        dfs(nums, new ArrayList<Integer>(), res);
        return res;
    }

    private void dfs(int[] nums, List<Integer> permutation, List<List<Integer>> res) {
        if (permutation.size() == nums.length) {
            res.add(new ArrayList<Integer>(permutation));
        }

        for (int i = 0; i < nums.length; i++) {
            if (permutation.contains(nums[i])) continue;
            permutation.add(nums[i]);
            dfs(nums, permutation, res);
            permutation.remove(permutation.size() - 1);
        }
    }
}
