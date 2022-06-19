"""
Given an m x n picture consisting of black 'B' and white 'W' pixels, return the number of black lonely pixels.

A black lonely pixel is a character 'B' that located at a specific position where the same row and same column don't have any other black pixels.

 

Example 1:


Input: picture = [["W","W","B"],["W","B","W"],["B","W","W"]]
Output: 3
Explanation: All the three 'B's are black lonely pixels.
Example 2:


Input: picture = [["B","B","B"],["B","B","W"],["B","B","B"]]
Output: 0
"""

class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        col_cnt = collections.defaultdict(int)
        row_cnt = collections.defaultdict(int)
        for i in range(len(picture)):
            for j in range(len(picture[0])):
                if picture[i][j] == "B":
                    row_cnt[i] += 1
                    col_cnt[j] += 1
        cnt = 0
        for i in range(len(picture)):
            for j in range(len(picture[0])):
                if picture[i][j] == "B":
                    if row_cnt[i] == 1 and col_cnt[j] == 1:
                        cnt += 1
        return cnt


