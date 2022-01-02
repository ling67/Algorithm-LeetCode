/*
Description
Given an integer array, find a subarray where the sum of numbers is zero. Your code should return the index of the first number and the index of the last number.

There is at least one subarray that it's sum equals to zero.

Example
Example 1:

Input:  [-3, 1, 2, -3, 4]
Output: [0, 2] or [1, 3].
Explanation: return anyone that the sum is 0.
*/


public class Solution {
    /**
     * @param nums: A list of integers
     * @return: A list of integers includes the index of the first number and the index of the last number
     */
    public List<Integer> subarraySum(int[] nums) {
        // write your code here
        int len = nums.length;

        List<Integer> result = new ArrayList<Integer>();
        Map<Integer, Integer> map = new HashMap<Integer, Integer>();

        map.put(0, -1);
        int sum = 0;

        for (int i = 0; i < len; i++) {
            sum += nums[i];
            if (map.containsKey(sum)) {
                result.add(map.get(sum) + 1);  // 思考下[-3, 1, 2, -3, 4]，输出[1, 3]，思考下就知道为什么要+1了
                result.add(i);
                return result;
            }
            map.put(sum, i);
        }
        return result;
    }
}

