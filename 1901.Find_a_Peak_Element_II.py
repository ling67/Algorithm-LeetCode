"""
A peak element in a 2D grid is an element that is strictly greater than all of its adjacent neighbors to the left, right, top, and bottom.

Given a 0-indexed m x n matrix mat where no two adjacent cells are equal, find any peak element mat[i][j] and return the length 2 array [i,j].

You may assume that the entire matrix is surrounded by an outer perimeter with the value -1 in each cell.

You must write an algorithm that runs in O(m log(n)) or O(n log(m)) time.

 

Example 1:



Input: mat = [[1,4],[3,2]]
Output: [0,1]
Explanation: Both 3 and 4 are peak elements so [1,0] and [0,1] are both acceptable answers.
Example 2:



Input: mat = [[10,20,15],[21,30,14],[7,16,32]]
Output: [1,1]
Explanation: Both 30 and 32 are peak elements so [1,1] and [2,2] are both acceptable answers.
 

Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 500
1 <= mat[i][j] <= 105
No two adjacent cells are equal.
"""

"""
solution1:iterative for loop to check every element in array  O(n^2)
solution2:     O(nlogn) each time remove half element in 2D array, Time complexity: O(nlogn), because in every binary search, we need O(n) is to find the max col idx in a row
solution3:     O(n) 
"""
class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        start, end = 0, len(mat) - 1   #row index
        while start + 1 < end:
            mid = start + (end - start) // 2
            max_col = self.find(mat[mid])
            if mat[mid][max_col] > mat[mid-1][max_col] and mat[mid][max_col] > mat[mid+1][max_col]:
                return [mid, max_col]
            elif mat[mid-1][max_col] > mat[mid][max_col]:   # up element larger than curr element
                end = mid
            else:
                start = mid
                
        start_idx = self.find(mat[start])
        end_idx = self.find(mat[end])
        
        return [end, end_idx] if mat[start][start_idx] < mat[end][end_idx] else [start, start_idx]
        
    def find(self, array):
        col = 0
        for i in range(1, len(array)):
            if array[i] > array[col]:
                col = i
        return col
