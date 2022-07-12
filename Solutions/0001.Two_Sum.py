/*
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

*/

//version 1: brute force
class Solution:
   def twoSum(self, nums: List[int], target: int) -> List[int]:
       n = len(nums)
       for i in range(n - 1):
           for j in range(i + 1, n):
               if nums[i] + nums[j] == target:
                   return [i, j]
       return [-1, -1]

// version 2: two pointer, 如果要返回index，就有问题~
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        i, j = 0, len(nums) - 1
        while i < j:
            sum = nums[i] + nums[j]
            if sum == target:
                return [i, j]
            elif sum > target:
                j -= 1
            else:
                i += 1
        return [-1, -1]
      
//version 3 : hashmap
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_idx = defaultdict(int)  #store [num, index]
        for idx, num in enumerate(nums):
            if target - num in num_idx:
                return [num_idx[target - num], idx]
            else:
                num_idx[num] = idx
        return [-1, -1]

/*****************************************Java version**************************************/       
class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> map = new HashMap();
        for(int i = 0; i < nums.length; i++){
            int complement = target - nums[i];
            if (map.containsKey(complement)) {
                return new int[] {i, map.get(complement)};
            }
            map.put(nums[i], i);
        }
        return null;
    }
}

//version 2 : two pointers
class Solution {
    
    class Pair implements Comparable<Pair> {
        int number, index;
        
        public Pair(int number, int index) {
            this.number = number;
            this.index = index;
        }
        
        public int compareTo(Pair other) {
            return number - other.number;
        }
    }
    
    public int[] twoSum(int[] nums, int target) {
        int[] result = {-1, -1};
        if (nums == null || nums.length == 0) {
            return null;
        }
        
        Pair[] pairs = getSortedPairs(nums);
        int left = 0, right = nums.length - 1; 
        while (left < right) {
            if (pairs[left].number + pairs[right].number == target) {
                result[0] = Math.min(pairs[left].index, pairs[right].index);
                result[1] = Math.max(pairs[left].index, pairs[right].index);
                return result;
            } else if (pairs[left].number + pairs[right].number > target) {
                right--;
            } else {
                left++;
            }
        }
        return null;
    }
    
    Pair[] getSortedPairs(int[] nums) {
        Pair[] pairs = new Pair[nums.length];
        for (int i = 0; i < nums.length; i++) {
            pairs[i] = new Pair(nums[i], i);
        }
        Arrays.sort(pairs);
        return pairs;
    }
}






