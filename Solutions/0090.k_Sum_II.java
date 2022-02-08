/*
Description
Given n unique postive integers, number k (1<=k<=n1<=k<=n) and target.

Find all possible k integers where their sum is target.

Wechat reply the 【90】 get the latest frequent Interview questions . (wechat id : jiuzhang15)

Example
Example 1:

Input:

array = [1,2,3,4]
k = 2
target = 5
Output:

[[1,4],[2,3]]
Explanation:

1+4=5,2+3=5

Example 2:

Input:

array = [1,3,4,6]
k = 3
target = 8
Output:

[[1,3,4]]
Explanation:

1+3+4=8
*/

public class Solution {
    /**
     * @param A: an integer array
     * @param k: a postive integer <= length(A)
     * @param target: an integer
     * @return: A list of lists of integer
     */
    public List<List<Integer>> kSumII(int[] A, int k, int target) {
        // write your code here
        List<List<Integer>> result = new ArrayList<>();
        dfs(A, k, target, 0, new ArrayList<Integer>(), result);
        return result;
    }

    private void dfs(int[] nums,
                    int k,
                    int target,
                    int startIndex,
                    List<Integer> combination,
                    List<List<Integer>> result) {

        //exit
        if (k == 0 && target == 0) {
            result.add(new ArrayList<Integer>(combination));
            return;
        }
        
        //exit
        if (k < 0) {
            return;
        }
        
        //拆分
        for (int i = startIndex; i < nums.length; i++) {
            if (nums[i] > target) {
                break;
            }
            
            combination.add(nums[i]);
            dfs(nums, k - 1, target - nums[i], i + 1, combination, result);
            combination.remove(combination.size() - 1);
        }                
    }

}
