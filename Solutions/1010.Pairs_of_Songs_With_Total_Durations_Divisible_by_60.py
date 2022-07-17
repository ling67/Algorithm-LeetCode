"""
You are given a list of songs where the ith song has a duration of time[i] seconds.

Return the number of pairs of songs for which their total duration in seconds is divisible by 60. Formally, we want the number of indices i, j such that i < j with (time[i] + time[j]) % 60 == 0.

 

Example 1:

Input: time = [30,20,150,100,40]
Output: 3
Explanation: Three pairs have a total duration divisible by 60:
(time[0] = 30, time[2] = 150): total duration 180
(time[1] = 20, time[3] = 100): total duration 120
(time[1] = 20, time[4] = 40): total duration 60
Example 2:

Input: time = [60,60,60]
Output: 3
Explanation: All three pairs have a total duration of 120, which is divisible by 60.
 

Constraints:

1 <= time.length <= 6 * 104
1 <= time[i] <= 500
"""

#Solution 1: 0只能跟0配对，30只能跟30配对 n*(n-1)//2, 其他的 m*n

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        ct = Counter([t % 60 for t in time])
        res = 0
        res += ct[0] * (ct[0] -1) // 2
        res += ct[30] * (ct[30] - 1) // 2
        res += sum(ct[i] * ct[60 - i] for i in range(1, 30))
        return res

"""
nums = [time % 60 for time in times];
Now it's a two sum problem with target = 60
"""
"""
mod_dict {key: time[idx] % 60, val: how many idx have that mod}
Then it's a 2 sum problem
"""
#Solution 2：hashmap
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        nums = [t % 60 for t in time]
        
        num_dict = defaultdict(int)
        res = 0
        for num in nums:
            if num == 0:
                res += num_dict[0]
            else:
                res += num_dict[60 - num]
            
            num_dict[num] += 1
        return res

#solution 3: two pointer

"""
mod_dict {key: time[idx] % 60, val: how many idx have that mod}
Then sort the mod_dict, then use two pointers.
"""
class Solution:
    def numPairsDivisibleBy60(self, times: List[int]) -> int:
        mod_dict = defaultdict(int)
        for time in times:
            mod_dict[time % 60] += 1
            
        key_lst = sorted(mod_dict)      # O(NlogN)
        
        i, j = 0, len(key_lst) - 1
        res = 0
        while i < j:
            if key_lst[i] + key_lst[j] < 60:
                i += 1
            elif key_lst[i] + key_lst[j] > 60:
                j -= 1
            else:
                res += mod_dict[key_lst[i]] * mod_dict[key_lst[j]]
                i += 1
                j -= 1
        
        # At last, we have to handle case where mod == 30 and mod == 0
        return res + (mod_dict[30] * (mod_dict[30] - 1)) // 2 + (mod_dict[0] * (mod_dict[0] - 1)) // 2
