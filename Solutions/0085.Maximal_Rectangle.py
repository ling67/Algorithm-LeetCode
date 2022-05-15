"""
Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

 

Example 1:


Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 6
Explanation: The maximal rectangle is shown in the above picture.
Example 2:

Input: matrix = [["0"]]
Output: 0
Example 3:

Input: matrix = [["1"]]
Output: 1
"""


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        heights = [0 for _ in range(n)]
        max_area = 0
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "0":
                    heights[j] = 0
                else:
                    heights[j] += 1
            max_area = max(max_area, self.get_max_area(heights))
        return max_area

    def get_max_area(self, heights):
        max_area = float('-inf')
        n = len(heights)
        
        #像右找第一个小于当前元素的num,单调递增栈
        r_idx = [-1 for _ in range(n)]
        st = [] #单调递增栈，存储(num, pos)
        for i, h in enumerate(heights):
            while len(st) > 0 and st[-1][0] > h:
                r_idx[st.pop()[1]] = i
            st.append((h, i))
        
        #像左找第一个小于当前元素的num,单调递增栈
        l_idx = [-1 for _ in range(n)]
        st = [] #单调递增栈，存储(num, pos)
        for i in range(n-1, -1, -1):
            while len(st) > 0 and st[-1][0] > heights[i]:
                l_idx[st.pop()[1]] = i
            st.append((heights[i], i))
            
        for i in range(n):
            if r_idx[i] == l_idx[i] == -1:
                max_area = max(max_area, heights[i] * n)
            elif r_idx[i] != -1 and l_idx[i] != -1:
                max_area = max(max_area, heights[i] * (r_idx[i] - l_idx[i] - 1))
            elif r_idx[i] == -1:
                max_area = max(max_area, heights[i] * (n - 1 - l_idx[i] ))
            elif l_idx[i] == -1:
                max_area = max(max_area, heights[i] * r_idx[i])
                
        return max_area

