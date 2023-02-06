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

//写的很麻烦
class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> results = new ArrayList();
        if (candidates == null || candidates.length == 0) {
            return results;
        }
        
        //先排序
        Arrays.sort(candidates);
        
        //限制了组合中的数之和
        help(candidates, 0, new ArrayList<Integer>(), target, results);
        return results;
    }
    
    //1.definition
    //从nums中的startIndex开始挑选一些数，放到combination中，且他们的和为target
    private void help(int[] nums,
                      int startIndex,
                      List<Integer> combination,
                      int target,
                      List<List<Integer>> results) {
        //3.exit 递归的出口
        if(target == 0) {
            //deep copy
            results.add(new ArrayList<Integer>(combination));
            return;
        }
        
        //2.split 递归的拆解
        //[1,2], [1,3] [1,4] [1,5]
        for (int i = startIndex; i < nums.length; i++) {
            if (nums[i] > target) {
                break;
            } 
            
            //[1] -> [1,2]
            combination.add(nums[i]);
            //把所有[1,2]开头的（剩余的）和为remainTarget的集合都找到，放到results；
            help(nums, i, combination, target - nums[i], results);  //combination sum 一个数可以选很多次
            //[1,2] -> [1]
            combination.remove(combination.size() -1);   
        }
    }    
}

//去重方法：两个指针，一个指针遍历，一个指针左边永远是去重好的数组
private int[] removeDuplicates(int[] candidates) {
        Arrays.sort(candidates);
        
        int index = 0;
        for (int i = 0; i < candidates.length; i++) {
            if (candidates[i] != candidates[index]) {
                candidates[++index] = candidates[i];
            }
        }
        
        int[] nums = new int[index + 1];
        for (int i = 0; i < index + 1; i++) {
            nums[i] = candidates[i];
        }
        
        return nums;
    }
