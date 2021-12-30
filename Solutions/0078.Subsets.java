class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> results = new ArrayList<>();
        Arrays.sort(nums);
        dfs(nums, 0, new ArrayList<Integer>(), results);
        return results;
    }
    
    //1.definition，Java对象传递时传的是引用，而不是值，所以在子函数中改变对象的值，调用函数也会改变
    private void dfs(int[] nums, int index, ArrayList<Integer> subset, List<List<Integer>> results) {
        
        //3.exit
        if (index == nums.length) {
            results.add(new ArrayList<Integer>(subset));  //这里必须新建ArrayList，而不是直接赋值，因为subset会变
            return;
        }
        
        //2.split
        
        //选择nums[index]
        subset.add(nums[index]);
        dfs(nums, index + 1, subset, results);
        
        //不选择nums[index]
        subset.remove(subset.size() - 1);
        dfs(nums, index + 1, subset, results);
        
    }
}
