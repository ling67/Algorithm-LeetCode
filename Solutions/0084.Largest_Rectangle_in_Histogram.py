"""
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

 

Example 1:


Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.
Example 2:


Input: heights = [2,4]
Output: 4

"""

"""
1.暴力解法：w*h，得到所有的矩形的面积，遍历得到最大的值。
2.栈解法：固定h，向左右扩散，向左边如果高度大于等于当前h，就加入这个面积，如果高度小于当前的高度就不加入，那此时的面积就是h*(j-i).
向左/右寻找第一个比自己小的位置可以用两次单调栈实现，我们可以把向左和向右第一个比自己小的位置存到起来，然后再来计算面积。
"""

"""
更省空间的解法，一次遍历求最大值
"""
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # save index in the monoStack, as height may have the same value
        # based on the heights, maintain an increasing stack (相等也可以)
        monoStack = [-1]        # 最左边放一个dummy height
        heights.append(-1)
        res = 0
        
        for idx, val in enumerate(heights):
            while heights[monoStack[-1]] > val:
                height = heights[monoStack.pop()]
                res = max(res, height * (idx - monoStack[-1] - 1))
                
            monoStack.append(idx)
        
        return res

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        
        #寻找向右的第一个比他小的元素
        st = []  #单调递增栈，小于就出站，大于就入栈 (num, index)
        r_pos = [-1 for _ in range(n)]
        for idx, h in enumerate(heights):
            while len(st) > 0 and st[-1][0] > h:
                r_pos[st[-1][1]] = idx
                st.pop()
            st.append((h, idx))
        
        #寻找向左的第一个比他小的元素
        st = []  #单调递增栈，小于就出站，大于就入栈 (num, index)
        l_pos = [-1 for _ in range(n)]
        for idx in range(n - 1, -1, -1):
            while len(st) > 0 and st[-1][0] > heights[idx]:
                l_pos[st[-1][1]] = idx
                st.pop()
            st.append((heights[idx], idx))

        maxValue = 0
        res = []
        for index, num in enumerate(heights):
            if r_pos[index] != -1 and l_pos[index] != -1:
                maxValue = max(maxValue, num * (r_pos[index] - l_pos[index] - 1))
            elif r_pos[index] == -1 and l_pos[index] == -1:
                maxValue = max(maxValue, num * n)
            elif r_pos[index] == -1:
                maxValue = max(maxValue, num * (n - 1 - l_pos[index]) )
            elif l_pos[index] == -1:
                maxValue = max(maxValue, num * r_pos[index])
        
        return maxValue
            
