/*
Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
 

Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
*/

class Solution {
    public List<List<Integer>> subsetsWithDup(int[] nums) {
        List<List<Integer>> results = new ArrayList<>();
        if (nums == null || nums.length == 0) {
            return results;
        }
        
        Arrays.sort(nums); 
        help(nums, 0, new ArrayList<Integer>(), results);
        return results;
    }
    
    //递归定义 
    private void help(int[] nums,
                      int startIndex,
                      List<Integer> subset,
                      List<List<Integer>> results) {
        //deep copy subset & add to results, 每次进入都将subset赋值进去，说明短的子集在前面
        results.add(new ArrayList<Integer>(subset));
        
        for (int i = startIndex; i < nums.length; i++) {
            //去重关键点要理解，1.前面一个没选中，2.当前nums[i] == nums[i-1] 这个点就不能选择，意思是不管选择几个重复的元素都是只能选择前面几个挨着的
            if ( i != startIndex && nums[i-1] == nums[i]) {
                continue;
            }
            subset.add(nums[i]);
            help(nums, i + 1, subset, results);
            subset.remove(subset.size() - 1);
        }
    }
    
}


