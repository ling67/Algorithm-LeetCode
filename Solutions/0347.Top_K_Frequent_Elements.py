/*
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
 

Constraints:

1 <= nums.length <= 105
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.

*/

//python version
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #先转成计数器
        q = []
        for num, freq in Counter(nums).items():
            if len(q) < k:
                heappush(q, (freq, num))
            else:
                heappushpop(q, (freq, num))
        return [x[1] for x in q]

       
/****************************************************java version****************************************************8/       
class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        //Prioraty
        Map<Integer, Integer> map = new HashMap<>();
        
        for (int i : nums) {
            map.put(i, map.getOrDefault(i, 0) + 1);
        }
        //PriorityQueue比较器使用方法：b.getValue大于a.getValue时b排在前面， lambda表达式相当于一个匿名方法，无方法名
        //https://www.codenong.com/cs105887131/
        PriorityQueue<Map.Entry<Integer, Integer>> pq = new PriorityQueue<>((a, b) -> b.getValue() - a.getValue());
        for (Map.Entry entry : map.entrySet()) {
            pq.add(entry);
        }
        int[] output = new int[k];
        for (int i = 0; i< k; i++) {
            output[i] = pq.poll().getKey();
        }
        return output;
    }
}
