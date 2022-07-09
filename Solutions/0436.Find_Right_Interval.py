"""
You are given an array of intervals, where intervals[i] = [starti, endi] and each starti is unique.

The right interval for an interval i is an interval j such that startj >= endi and startj is minimized. Note that i may equal j.

Return an array of right interval indices for each interval i. If no right interval exists for interval i, then put -1 at index i.

 

Example 1:

Input: intervals = [[1,2]]
Output: [-1]
Explanation: There is only one interval in the collection, so it outputs -1.
Example 2:

Input: intervals = [[3,4],[2,3],[1,2]]
Output: [-1,0,1]
Explanation: There is no right interval for [3,4].
The right interval for [2,3] is [3,4] since start0 = 3 is the smallest start that is >= end1 = 3.
The right interval for [1,2] is [2,3] since start1 = 2 is the smallest start that is >= end2 = 2.
Example 3:

Input: intervals = [[1,4],[2,3],[3,4]]
Output: [-1,2,-1]
Explanation: There is no right interval for [1,4] and [3,4].
The right interval for [2,3] is [3,4] since start2 = 3 is the smallest start that is >= end1 = 3.
 

Constraints:

1 <= intervals.length <= 2 * 104
intervals[i].length == 2
-106 <= starti <= endi <= 106
The start point of each interval is unique.
"""

"""
先按左节点排序，加入排序的序号
然后用二分依次搜索每一个range的右边区间
参考: https://www.youtube.com/watch?v=fEVyHmO-KF8
"""
class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        intervals = sorted((e[0], i, e[1]) for i, e in enumerate(intervals))
        l = len(intervals)
        res = [0] * l
        for e in intervals:
            r = bisect.bisect_left(intervals, (e[2],))
            res[e[1]] = intervals[r][1] if r < l else -1
        return res

