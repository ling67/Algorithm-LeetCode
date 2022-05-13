"""
Given an n x n matrix where each of the rows and columns is sorted in ascending order, return the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

You must find a solution with a memory complexity better than O(n2).

 

Example 1:

Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
Output: 13
Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the 8th smallest number is 13
Example 2:

Input: matrix = [[-5]], k = 1
Output: -5
 

Constraints:

n == matrix.length == matrix[i].length
1 <= n <= 300
-109 <= matrix[i][j] <= 109
All the rows and columns of matrix are guaranteed to be sorted in non-decreasing order.
1 <= k <= n2
 

Follow up:

Could you solve the problem with a constant memory (i.e., O(1) memory complexity)?
Could you solve the problem in O(n) time complexity? The solution may be too advanced for an interview but you may find reading this paper fun.
"""

"""
1.brute force 变成1D, 排序 ->N^2*logN
2.将2d变成1d, 参考0215  ->N^2*logK  比方法1小一点
3. 对于任意一个位置(i,j),我们知道(1+1，j),(i, j + 1) 一定比当前数大，展开搜索BFS
    起点：(0,0) 每次展开最小值
    https://www.youtube.com/watch?v=Lo23qFLhJNY
    
    利用sorted matrix的性质，从左上角第一个元素开始，添加进heap，然后heap当然自动排序了，然后pop出最小的，然后把最小的那个数的右边和下边的元素分别入heap，这样可以保证每次pop出来的都是最小的。
O(Klog(K) 

"""
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        hq = []
        added = set()    #store the idx that has already been added into hq
        heappush(hq, (matrix[0][0], (0,0)))  #(i, j)也要放进hq
        added.add((0, 0)) #注意这里的visited不能存储matrix[i][j], 因为不同的地方可能存在相同的数, 容易错，set增加应该用add()
        
        m, n = len(matrix), len(matrix[0])
        res = matrix[0][0]
        for _ in range(k):   #O(klogk)
            res, idx = heappop(hq)
            i, j = idx[0], idx[1]
            if i+1<m and (i+1, j) not in added:
                heappush(hq, (matrix[i+1][j], (i+1, j)))
                added.add((i+1, j))
            if j+1<n and (i, j+1) not in added:
                heappush(hq, (matrix[i][j+1], (i, j+1)))
                added.add((i, j+1))
        return res
