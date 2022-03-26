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

//version python dfs + backtrack

"""
如果输入存在重复元素，[1, 2, 2]的遍历中，我们只取前面的那个2，对于后面的那个2，如果不是挨着前面那个2选的，也就是说 i != startIndex，那么就不要放后面那个2，这样会造成重复出现[1,第一个2],[1,第二个2], 注意可以挨着第一个2来选第二个2是可以的，因为允许出现[1,2,2]作为答案。所以contraint是: if (i >= 1 and nums[i] == nums[i-1]) and i != startIndex: continue
"""
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def backtrack(curr_idx, curr_subsets):
            res.append(curr_subsets.copy())     #has to be a deep copy
            for next_idx in range(curr_idx + 1, len(nums)):   #不允许一个数取多次，则next candidate从i+1开始
                if next_idx > 0 and nums[next_idx] == nums[next_idx - 1] and next_idx != curr_idx + 1:    #注意：这里的判断条件
                    continue
                curr_subsets.append(nums[next_idx])
                backtrack(next_idx, curr_subsets)
                curr_subsets.pop()
        
        nums.sort()      # 去重step 1: sort the nums!!!!
        res = []
        backtrack(-1, [])  #注意从-1开始
        return res
    


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


