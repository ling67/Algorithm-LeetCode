"""
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

 

Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
Example 3:

Input: temperatures = [30,60,90]
Output: [1,1,0]
 

Constraints:

1 <= temperatures.length <= 105
30 <= temperatures[i] <= 100
"""

"""
求右边第一个比当前大的就是单调递减栈
st = [0 for _ in range(len())]
存入index, count
"""
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        st = []
        res = [0 for _ in range(n)]
        
        for index, temp in enumerate(temperatures):
            while len(st) > 0 and temp > st[-1][1]:
                num = st.pop()
                res[num[0]] = index - num[0]  #注意这里容易错，求的是index之差
            st.append((index, temp))
            
        return res    
        

