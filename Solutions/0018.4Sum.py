"""
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

 

Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
Example 2:

Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]
 

Constraints:

1 <= nums.length <= 200
-109 <= nums[i] <= 109
-109 <= target <= 109
"""

# Solution 1: HashSet 对结果去重
"""
The idea is to use HashSet to track past elements.
We iterate the combinations of nums[i], nums[j], nums[k], and calculate the last number by lastNumber = target - nums[i] - nums[j] - nums[k].
We check if lastNumber is existed the past by checking in the HashSet, if existed, then it form a quadruplets then add it to the answer.
Complexity:
Time: O(N^3)
Extra Space (Without count output as space): O(N)
"""
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        seen = set()
        ans = set()
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    lastNumber = target - nums[i] - nums[j] - nums[k]
                    if lastNumber in seen:
                        arr = sorted([nums[i], nums[j], nums[k], lastNumber])
                        ans.add((arr[0], arr[1], arr[2], arr[3]))
            seen.add(nums[i])
        return ans

# Solution 2: two pointer  对结果去重
"""
Sort nums in increasing order.
We fix nums[i], nums[j] by iterating the combination of nums[i], nums[j], then the problem now become to very classic problem 1. Two Sum.
By using two pointers, one points to left, the other points to right, remain = target - nums[i] - nums[j].
If nums[left] + nums[right] == remain Found a valid quadruplets
Else if nums[left] + nums[right] > remain  Sum is bigger than remain, need to decrease sum by right -= 1
Else: Increasing sum by left += 1.

Complexity:
Time: O(N^3)
Extra Space (Without count output as space): O(sorting)
"""
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = set()
        for i in range(n):
            for j in range(i+1, n):
                l, r = j + 1, n - 1
                remain = target - nums[i] - nums[j]
                while l < r:
                    if nums[l] + nums[r] == remain:
                        ans.add((nums[i], nums[j], nums[l], nums[r]))
                        l += 1
                        r -= 1
                    elif nums[l] + nums[r] > remain:
                        r -= 1
                    else:
                        l += 1
        return ans


# Solution 3: two pointer  对过程去重

"""for循环nums[i]，然后for循环nums[j]，在用双指针解决twoSum问题 O(N^3), O(1)"""
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if not nums or len(nums) < 4:
            return []
        
        nums.sort()
        
        res = []
        lens = len(nums)
        
        for i in range(lens-3):
            if i > 0 and nums[i] == nums[i-1]:  #去重 易错点
                continue
            
            if nums[i] * 4 > target:  #优化
                break
                
            for j in range(i+1, lens-2):
                # 注意这里给j去重不能从j>=1开始，因为要至少让j先取上第一个值i+1之后才能与前一个数比较！不然[0,0,0,], 0就通不过了。
                
                if j > i + 1 and nums[j] == nums[j-1]:  
                    continue
                    
                if nums[i] + nums[j] * 3 > target: #优化  易错点：记得加上nums[i]
                    break
                
                left, right = j + 1, lens - 1
                while left < right:
                    fourSum = nums[i] + nums[j] + nums[left] + nums[right]
                    if fourSum > target:
                        right -= 1
                    elif fourSum < target:
                        left += 1
                    else:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1              #易错点：记得先处理left and right 再去重
                        right -= 1
                        while left < right and nums[left] == nums[left - 1]:  #去重
                            left += 1 
                        while left < right and nums[right] == nums[right + 1]:  #去重
                            right -= 1
        return res

# Solution 4: Ksum 的通用写法

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res, quad = [], []
        
        def kSum(k, start, target):
            if k != 2:
                for i in range(start, len(nums) - k + 1):
                    if i > start and nums[i] == nums[i - 1]:
                        continue
                    quad.append(nums[i])
                    kSum(k - 1, i + 1, target - nums[i])
                    quad.pop()   #好像就是backtrack
                return 
            
            l, r = start, len(nums) - 1
            while l < r:
                if nums[l] + nums[r] < target:
                    l += 1
                elif nums[l] + nums[r] > target:
                    r -= 1
                else:
                    res.append(quad + [nums[l], nums[r]])
                    l += 1        
                    while l < r and nums[l] == nums[l - 1]:   #因为上面一行没有移动r，所以这里也不需要对r去重
                        l += 1
        kSum(4, 0, target)
        return res
            
       
