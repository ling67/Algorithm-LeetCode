/*
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

*/


/*
1.brute force
2.sort
3.hashset
*/

//version3 python版本
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_streak = 0
        num_set = set(nums)
        
        for num in num_set:
            if num - 1 not in num_set:
                curr_num = num
                curr_streak = 1
                
                while curr_num + 1 in num_set:
                    curr_num += 1
                    curr_streak += 1
                    
                longest_streak = max(longest_streak, curr_streak)
        return longest_streak
       

//version3 有时间可以做下V1和V2
class Solution {
    public int longestConsecutive(int[] nums) {
        Set<Integer> num_set = new HashSet<Integer>();
        for (int num : nums) {
            num_set.add(num);
        }
        
        int longestStreak = 0;
        
        for (int num : num_set) {
            //不包含num-1
            if (!num_set.contains(num-1)) {
                int currentNum = num;
                int currentStreak = 1;
                
                while (num_set.contains(currentNum+1)) {
                    currentNum += 1;
                    currentStreak += 1;
                }
                longestStreak = Math.max(longestStreak, currentStreak);
            }
        }
        return longestStreak;
    }
}

