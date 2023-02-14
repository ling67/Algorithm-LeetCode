class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        if (nums == null || nums.length == 0) return res;
        dfs(nums, 0, new ArrayList<Integer>(), res);
        return res;
    }

    //递归的定义
    //在nums中找到所有以subset开头的集合，并放到resuts中
    private void dfs(int[] nums, int startIndex, List<Integer> subsets, List<List<Integer>> res) {
        //递归的拆解
        res.add(new ArrayList<Integer>(subsets));
        for (int i = startIndex; i < nums.length; i++) {
            subsets.add(nums[i]);
            dfs(nums, i + 1, subsets, res);
            subsets.remove(subsets.size() - 1);
        }
        //出口
    }
}
