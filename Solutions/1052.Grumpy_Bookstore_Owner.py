"""
There is a bookstore owner that has a store open for n minutes. Every minute, some number of customers enter the store. You are given an integer array customers of length n where customers[i] is the number of the customer that enters the store at the start of the ith minute and all those customers leave after the end of that minute.

On some minutes, the bookstore owner is grumpy. You are given a binary array grumpy where grumpy[i] is 1 if the bookstore owner is grumpy during the ith minute, and is 0 otherwise.

When the bookstore owner is grumpy, the customers of that minute are not satisfied, otherwise, they are satisfied.

The bookstore owner knows a secret technique to keep themselves not grumpy for minutes consecutive minutes, but can only use it once.

Return the maximum number of customers that can be satisfied throughout the day.

 

Example 1:

Input: customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], minutes = 3
Output: 16
Explanation: The bookstore owner keeps themselves not grumpy for the last 3 minutes. 
The maximum number of customers that can be satisfied = 1 + 1 + 1 + 1 + 7 + 5 = 16.
Example 2:

Input: customers = [1], grumpy = [0], minutes = 1
Output: 1
 

Constraints:

n == customers.length == grumpy.length
1 <= minutes <= n <= 2 * 104
0 <= customers[i] <= 1000
grumpy[i] is either 0 or 1.
"""

"""
The first intuition is to find the larget lens in arr grumpy with at most X 0s.
Then realized we need to find the largest number of customers with at most X 0s.
Since the window size is fixed, the problem is easier to implement. We only need to update the max_gain,
which represents how man ymore people can be satisfied if the owner use X minites magic card
"""

class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        satisfy = sum(customers[i] for i in range(len(customers)) if grumpy[i] == 0)
        max_satisfy = satisfy
        for i, ch in enumerate(customers):
            if grumpy[i] == 1:
                satisfy += customers[i]
            
            if i >= minutes:
                if grumpy[i - minutes] == 1:
                    satisfy -= customers[i - minutes]
                
            if i >= minutes - 1:        #这个可有可无，因为是求最大值
                max_satisfy = max(max_satisfy, satisfy)
              
        return max_satisfy
      
