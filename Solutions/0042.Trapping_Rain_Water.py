"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

 

Example 1:


Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9
 

Constraints:

n == height.length
1 <= n <= 2 * 104
0 <= height[i] <= 105
"""

"""
山景城一姐de讲解：首先找到最高highestBar的位置。然后从左边往最高的位置扫，同时maintain一个指针记录leftHighest的高度，如果扫到的地方i小于这个leftHighest的高度，
则说明i这个地方可以蓄水，可蓄水量为leftHighest的高度减去i的高度；如果扫到的地方i大于这个leftHighest的高度，则说明i这个地方不可以蓄水，
因为水会从左边溜走，所以这时候要更新leftHighest为i的高度。同理对右边做同样的操作
O(N), O(1)
"""
class Solution:
    def trap(self, height: List[int]) -> int:
        #step1: find the highestBar
        highestBar = 0
        highestBarPos = 0
        for i, bar in enumerate(height):
            if bar > highestBar:
                highestBarPos = i
                highestBar = bar
        
        #step2: scan the left part
        water = 0
        leftHighest = 0
        for i in range(highestBarPos):
            if height[i] > leftHighest:
                leftHighest = height[i]
            else:
                water += leftHighest - height[i]
        
        #step3: scan the right part
        rightHighest = 0
        for i in range(len(height) - 1, highestBarPos, -1):
            if height[i] > rightHighest:
                rightHighest = height[i]
            else:
                water += rightHighest - height[i]
        
        return water
        
