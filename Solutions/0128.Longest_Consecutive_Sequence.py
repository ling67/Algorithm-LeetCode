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
"""
使用一个集合hashset存入所有的数字，然后遍历数组中的每个数字，如果其在集合中存在，那就将其移除，然后分别用两个变量pre
和next算出其前一个跟后一个数。
注意：找到后要删除set中的数，因为没有必要再重复的寻找最大的连续序列，例如4231，找了4的最大连续序列，就不用再找了
"""
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        max_cnt = 0
        for num in nums:
            if num in numset:  
                numset.remove(num)   #注意这里，找到后要删除set中的数，因为没有必要再重复的寻找最大的连续序列，例如4231，找了4的最大连续序列，就不用再找了
                cnt = 1
                
                prev = num - 1
                while prev in numset:
                    numset.remove(prev)
                    cnt += 1
                    prev -= 1
                    
                nxt = num + 1
                while nxt in numset:
                    numset.remove(nxt)
                    cnt += 1
                    nxt += 1
                    
                max_cnt = max(max_cnt, cnt)
            
        return max_cnt
            
"""
Follow up question: what if we can add a number into the nums list, 
and each time we add a number, we need to query the longest consecutive seqence?
Answer: we need to realize dynamic connection.  We can choose UnionFind.
需要query 点a所在集合的元素个数，所以需要用一个dictionary self.size 用来记录每个father节点所在集合的点的个数，
在union i 和 j 的时候: father[i] = j, sz[j] += sz[i].  
算法是我们遍历nums, 对于每一个num, 我们connect num and num-  1, also connect num and num + 1
"""       
class UnionFind:
        def __init__(self, nums):
            self.father = collections.defaultdict(int)
            self.size = collections.defaultdict(int)
            
            for num in nums:
                self.add(num)
                
        def add(self, x):
            self.father[x] = x
            self.size[x] = 1
            
        def find(self, x):
            if self.father[x] == x:
                return x
            else:
                self.father[x] = self.find(self.father[x])
                return self.father[x]
        
        def union(self, a, b):
            root_a, root_b = self.find(a), self.find(b)
            if root_a != root_b:
                self.father[root_a] = root_b
                self.size[root_b] += self.size[root_a]  # 更新root_b的size
        
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        uf = UnionFind(nums)
        for num in nums:
            if num - 1 in uf.father:
                uf.union(num, num - 1)
            if num + 1 in uf.father:
                uf.union(num, num + 1)
        return max(sz for _, sz in uf.size.items())
    
       

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

